import requests
from bs4 import BeautifulSoup

uri = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"

response = requests.get(uri)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

target = soup.select_one(".todaytemp")

print(target.text)
