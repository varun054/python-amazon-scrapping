import requests
from bs4 import BeautifulSoup

header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
'Accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,/;q=0.8',
'Accept-Language': 'en-GB,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Dnt': '1',
'Priority': 'u=1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrage-Insecure-Requests': '1',
}
response = requests.get('https://www.amazon.in/Subaa-Kalvam-Mortar-Khalbatta-Kitchen/dp/B0DDCWYRKK/', headers=header)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
print(price)