#!/usr/bin/python3
# 98.py
# Danisile Jiyane <danisilejiyane2@gmail.com>
"""Hodor with my Holberton ID 98 times."""
import requests
from bs4 import BeautifulSoup


php = "http://158.69.76.135/level4.php"
proxy_sites = ["https://www.free-proxy-list.net/", "https://www.us-proxy.org/"]
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) "
              "Gecko/20100101 Firefox/64.0")
header = {
    "User-Agent": user_agent,
    "referer": php,
}
vote = {
    "id": "375",
    "holdthedoor": "Submit",
    "key": ""
}
proxy = {
    "http": "",
}


def get_vote_count(php, vote_id):
    """Return the current vote count of an ID.

    Args:
        php (string): The voting website to check.
        vote_id (string): The Holberton ID to get the vote count of.
    """
    page = requests.get(php)
    soup = BeautifulSoup(page.text, "html.parser")
    total = list(soup.find_all("td"))
    for i in range(len(total)):
        if vote_id in str(total[i].text):
            return int(total[i + 1].text[1:])
    return 0

if __name__ == "__main__":
    count = 0
    rotate = 0
    while count < 98:
        session = requests.session()
        page = session.get(proxy_sites[rotate])
        rotate = 1 if rotate == 0 else 0
        soup = BeautifulSoup(page.text, "html.parser")
        proxy_list = soup.find("tbody").find_all("tr")

        for ip in proxy_list:
            proxy["http"] = "http://" + ip.find("td").text
            print("Trying {}".format(proxy["http"]))
            try:
                session = requests.session()
                page = session.get(php, headers=header, proxies=proxy,
                                   timeout=5)
                soup = BeautifulSoup(page.text, "html.parser")

                hidden_value = soup.find("form", {"method": "post"})
                hidden_value = hidden_value.find("input", {"type": "hidden"})
                vote["key"] = hidden_value["value"]

                session.post(php, headers=header, proxies=proxy,
                             data=vote, timeout=5)
                total = get_vote_count(php, vote["id"])
                if total > count:
                    print("... success! Vote count = {}".format(count))
                    count += 1
                else:
                    print("... failed.")
            except:
                print("... failed.")
