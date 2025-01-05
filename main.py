import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get('https://appbrewery.github.io/instant_pot/', headers=header)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
print(price.split("$")[1])