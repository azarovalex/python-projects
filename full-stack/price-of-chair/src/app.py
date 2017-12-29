import requests
from bs4 import BeautifulSoup

request = requests.get("https://catalog.onliner.by/headphones/beats/mlye2")

content = request.content

soup = BeautifulSoup(content, "html.parser")

element = soup.find("a", {"class": "offers-description__link offers-description__link_subsidiary offers-description__link_nodecor"})

stringPrice = element.text.strip()    # 270,00 – 329,00 р.

lowestPrice = int(stringPrice[:3])

print(lowestPrice)