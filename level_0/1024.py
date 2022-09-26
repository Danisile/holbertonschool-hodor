#!/usr/bin/python3
# 1024.py
# Thato Khosa <4502@holbertonschool.com>
"""Hodor with my Holberton ID 1024 times."""
import requests

php = "http://158.69.76.135/level0.php"
vote = {
    "id": "375",
    "holdthedoor": "Submit"
}

if __name__ == "__main__":
    for i in range(0, 1024):
        requests.post(php, data=vote)
