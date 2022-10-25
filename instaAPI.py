import requests
import json


def main():
    with open("config.json", "r") as cfg:
        config = json.loads(cfg.read())
    session = requests.Session()
    """resp = session.get("https://www.instagram.com/accounts/login/")
    csrf_token = resp.text[resp.text.index("csrf_token")+15: resp.text.index("csrf_token")+47]
    cookies = {
        "ig_did": "11B169A9-215F-4C42-8494-6E4CF865E61D",
        "ig_nrcb": "1",
        "datr": "w0pXY1i99pvmw7F9ZZFrJlmu",
        "rur": "\"NCG\\05411223919133\\0541698201421:01f755ae5ad1e6c7e7c96c9a882bf0ba29e8b975ffbd511f6f7901c387bbacdeb78b3edb\"",
        "shbid": "\"7175\\05411223919133\\0541698201326:01f718db16b995613914f3de4808cbe757673161799c1355762f5cc134e352603b225338\"",
        "shbts": "\"1666665326\\05411223919133\\0541698201326:01f785e253136decceac2065c7537abe0fce4112914b81e070da7ef86c1b3b779b8a461a\"",
        "csrftoken": csrf_token
    }
    data = {
        'enc_password': "#PWD_INSTAGRAM_BROWSER:10:1666666300:ASdQAOIIvjr4Hz4WufNA//JK5RtZazQcJ0+Nn3rSWPxHnuR6bnZxhlloWaLfJ3AF6pLgQIwxr6g90Ra99XBZHflh5pSWaFuZrhggutlwnsUzRHRMt/d0GdMMVJVigFMK/fKWFEt+JJt372f6m5IPE6Zh",
        'username': config["host"]["username"],
        'queryParams': "{}",
        'optIntoOneTap': "false",
        'trustedDeviceRecords': "{}"
    }
    resp2 = session.post("https://i.instagram.com/api/v1/web/accounts/login/ajax/", files=data, cookies=cookies)"""
    csrf_token = "UwYt4HJ0ZY1f8Mf9Nn3zGDopbX6eut3L"
    cookies = {
        "ig_did": "11B169A9-215F-4C42-8494-6E4CF865E61D",
        "ig_nrcb": "1",
        "datr": "w0pXY1i99pvmw7F9ZZFrJlmu",
        "rur": "\"NCG\\05411223919133\\0541698201421:01f755ae5ad1e6c7e7c96c9a882bf0ba29e8b975ffbd511f6f7901c387bbacdeb78b3edb\"",
        "shbid": "\"7175\\05411223919133\\0541698201326:01f718db16b995613914f3de4808cbe757673161799c1355762f5cc134e352603b225338\"",
        "shbts": "\"1666665326\\05411223919133\\0541698201326:01f785e253136decceac2065c7537abe0fce4112914b81e070da7ef86c1b3b779b8a461a\"",
        "csrftoken": csrf_token
    }
    headers = {
        "Accept": "*/*",
        "X-CSRFToken": csrf_token,
        "X-Instagram-AJAX": "1006449831",
        "X-IG-App-ID": "936619743392459",
        "X-ASBD-ID": "198387",
        "X-IG-WWW-Claim": "hmac.AR2qVhKGmtZ0jnEgLDcxBe5esV60Duyk-NGfPjO-PEyu5jYJ",
        "Origin": "https://www.instagram.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://www.instagram.com/",
        "Cookie": 'ig_did=85115E19-B0A8-4E1F-8F4C-265D66B9CF59;'
                  'datr=r2FXYwEsnHh9Z21EkGepU6ip;'
                  'csrftoken=UwYt4HJ0ZY1f8Mf9Nn3zGDopbX6eut3L;'
                  'ig_nrcb=1;'
                  'mid=Y1dhsAAEAAESANv1FmYavZeiI3-J;'
                  'rur="NCG\\05411223919133\\0541698207047:01f76816da0bcc420f059a4e5b7c92515d0915c3b9987825262e68fb96501b45ab5036a5";'
                  'sessionid=11223919133%3Ao57wF6XVvn4fv5%3A17%3AAYeUVspWxV_M_IEQCPJMe9VWnJ7Kt16WUxTUygJUbw;'
                  'ds_user_id=11223919133;'
                  'shbid="7175\\05411223919133\\0541698207034:01f77a80958522c2f765bd1c9cce9464205b55b247ced0b69207d52e5914414248aae7ec";'
                  'shbts="1666671034\\05411223919133\\0541698207034:01f7a787b24c750f7d6f5d718cae2f7115c7be8781aa3eeaaaa1d757f5057ca26fe8f143"'
    }
    """ig_did=85115E19-B0A8-4E1F-8F4C-265D66B9CF59;
    datr=r2FXYwEsnHh9Z21EkGepU6ip; 
    csrftoken=UwYt4HJ0ZY1f8Mf9Nn3zGDopbX6eut3L;
    ig_nrcb=1;
    mid=Y1dhsAAEAAESANv1FmYavZeiI3-J;
    rur="NCG\\05411223919133\\0541698256340:01f73eaedef0d4f77531da1c3eaed766a413d5a1a7f6e80fee99aeb54e58cf633bdf8864";
    sessionid=11223919133%3Ao57wF6XVvn4fv5%3A17%3AAYeUVspWxV_M_IEQCPJMe9VWnJ7Kt16WUxTUygJUbw;
    ds_user_id=<ID>;
    shbid="7175\\05411223919133\\0541698207034:01f77a80958522c2f765bd1c9cce9464205b55b247ced0b69207d52e5914414248aae7ec";
    shbts="1666671034\\05411223919133\\0541698207034:01f7a787b24c750f7d6f5d718cae2f7115c7be8781aa3eeaaaa1d757f5057ca26fe8f143\""""
    users = {config["host"]["user_id"]: "me"}
    chat_resp = session.get("https://i.instagram.com/api/v1/direct_v2/threads/"
                            "340282366841710300949128150560022781488/", headers=headers)
    thread = json.loads(chat_resp.text)['thread']
    for user in thread["users"]:
        users[user["pk"]] = user["username"]
    messages = []
    cursor = thread["oldest_cursor"]
    page = 0
    while True:
        print(f"Page {page}")
        for message in thread["items"]:
            if message["item_type"] == "text":
                messages.append({"user_id": message["user_id"], "item_type": message["item_type"],
                                "timestamp": message["timestamp"], "content": message["text"]})
        chat_resp = session.get("https://i.instagram.com/api/v1/direct_v2/threads/"
                                f"340282366841710300949128150560022781488?cursor={cursor}", headers=headers)
        thread = json.loads(chat_resp.text)['thread']
        page += 1

    print("Done")


if __name__ == '__main__':
    main()
