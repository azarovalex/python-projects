import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.onliner.by")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "_u"})

print(element.text)

# <span class="_u" data-bind="text: '$ ' + $root.amount">$ 2,0023</span>
