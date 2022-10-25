import traceback
from selenium import webdriver
from seleniumwire import webdriver
import os
import time
import json
import gzip
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


class ChatCrawler:
    def __init__(self, username, password, driver=None, login_retries=0):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com/direct/inbox/'
        self.activeUser = None
        login_count = login_retries
        # Retry multiple times if error in attempt
        while login_count >= 0:
            login_count -= 1
            try:
                # Firefox as default
                self.bot = webdriver.Firefox(executable_path=GeckoDriverManager().install()) if not driver else driver
                # Launch browser and log in
                self.login()
                break
            except Exception as e:
                self.bot.quit()

    def login(self):
        self.bot.get(self.base_url)
        # Submit credentials and log in
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        # Wait for page to load
        time.sleep(7)

        # Save Info popup
        self.bot.find_element(By.XPATH,
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)

        # Notification popup
        self.bot.find_element(By.XPATH,
            '/html/body/div[1]/div/div[1]/div/div[2]/div/div/'
            'div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
        time.sleep(4)

    def selectUser(self, scanUser):
        self.activeUser = scanUser
        # Create new chat icon
        self.bot.find_element(By.XPATH,
            '/html/body/div[1]/div/div[1]/div/div[1]/div/div/'
            'div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]'
            '/div/div[3]/button').click()
        time.sleep(2)
        # Search username
        self.bot.find_element(By.XPATH,
            '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/'
            'div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input').send_keys(scanUser)
        time.sleep(2)

        # Confirm username
        self.bot.find_element(By.XPATH,
            '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/'
            'div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]').click()
        time.sleep(2)

        # Submit for char creation
        self.bot.find_element(By.XPATH,
            '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]'
            '/div/div/div/div/div/div/div[1]/div/div[3]/div/button').click()
        time.sleep(2)

    def getMessages(self, max_messages=float('inf'), batch_size=1, retries=0, after_id=float('inf')):
        if not self.activeUser:
            return None
        # Select element containing messages
        element = self.bot.find_element(By.XPATH,
            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/"
            "div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div")
        # Keeps track of last request processed so the same is not processed twice
        lastReqTime = 0
        retry_attempts = retries
        gotten_messages = 0
        messages = []
        message_ids = []
        while gotten_messages < max_messages:
            scrolls = 3
            while scrolls > 0:
                scrolls -= 1
                self.bot.execute_script("""arguments[0].scroll({
                    top: 200,
                    behavior: 'auto'
                    });""", element)
                time.sleep(0.75)
            requests = self.bot.requests
            apiRequests = [req.response.body for req in requests if "direct_v2/threads" in req.url and
                           req.response is not None and datetime.timestamp(req.date) > lastReqTime]
            for idx, req in enumerate(apiRequests):
                try:
                    loaded = json.loads(gzip.decompress(req).decode())
                    users = {}
                    for thread_user in loaded["thread"]["users"]:
                        users[thread_user["pk"]] = thread_user["username"]
                    for item in loaded["thread"]["items"]:
                        try:
                            """if item["item_id"] in message_ids:
                                print(f'Duplicate message, {item["item_id"]}, {item["text"]}')"""
                            if int(item["item_id"]) <= after_id and item["item_id"] not in message_ids:
                                message_ids.append(item["item_id"])
                                messages.append({"item_id": item["item_id"], "user_id": item["user_id"],
                                    "user_name": users.get(item["user_id"], "me"), "text": item["text"]})
                        except:
                            pass
                except Exception as e:
                    pass
            if len(messages) == 0 and retry_attempts == 0:
                retry_attempts -= 1
                break
            lastReqTime = time.time()
            while len(messages) > 0:
                gotten_messages += 1
                if batch_size > 1:
                    batch = []
                    while len(batch) < batch_size:
                        batch.append(messages.pop(0))
                else:
                    batch = messages.pop(0)
                yield batch

    def quit(self):
        self.bot.quit()


def saveFile(fileName, messages):
    with open(fileName, "a") as file:
        for message in messages:
            file.write(str(message)+"\n")


def init():
    with open("config.json", "r") as cfg:
        config = json.loads(cfg.read())
    os.environ['GH_TOKEN'] = config["token"]
    bot = ChatCrawler(config["host"]["username"], config["host"]["password"], login_retries=0)
    bot.selectUser(config["target"]["username"])
    messages = []
    for msg in bot.getMessages(retries=2, max_messages=50):
        messages.append(msg)
    bot.quit()
    print(messages)
    saveFile(config["target"]["username"], messages)


if __name__ == '__main__':
    init()
