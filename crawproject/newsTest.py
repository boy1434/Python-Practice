import requests
from bs4 import BeautifulSoup

uri = f"https://newsstand.naver.com/?list=&pcode=005"

response = requests.get(uri)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

target = soup.select_one("#focusPanelCenter .panel_inner img")
title = target["alt"]
print(title)
