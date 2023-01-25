#!/usr/bin/python3
# 1024.py
#Danisile Jiyane<danisilejiyane2@gmail.com>
"""Hodor with my Holberton ID 1024 times."""
import os
import requests
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image
from bs4 import BeautifulSoup

php = "http://158.69.76.135/level3.php"
ip = "http://158.69.76.135"
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) "
              "Gecko/20100101 Firefox/64.0")
header = {
    "User-Agent": user_agent,
    "referer": php
}
vote = {
    "id": "375",
    "holdthedoor": "Submit",
    "key": "",
    "captcha": ""
}

if __name__ == "__main__":
    count = 0
    while count < 1024:
        session = requests.session()
        page = session.get(php, headers=header)
        soup = BeautifulSoup(page.text, "html.parser")

        hidden_value = soup.find("form", {"method": "post"})
        hidden_value = hidden_value.find("input", {"type": "hidden"})
        vote["key"] = hidden_value["value"]

        captcha_path = soup.find("form", {"method": "post"}).find("img")
        captcha_path = ip + captcha_path["src"]
        captcha_img = open("captcha.png", "wb")
        captcha_img.write(session.get(captcha_path).content)
        captcha_img.close()
        captcha_php = pytesseract.image_to_string("captcha.png")
        os.remove("captcha.png")
        vote["captcha"] = captcha_php

        r = session.post(php, headers=header, data=vote)
        if str(r.content) != "b'See you later hacker! [11]'":
            count += 1
