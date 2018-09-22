import requests
from bs4 import BeautifulSoup

html = requests.get("https://itoppy18.github.io/code/wii.html")
soup = BeautifulSoup(html.text, "html.parser")
print(soup.p.string)

