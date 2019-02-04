from bs4 import BeautifulSoup
import re
import requests

URL='https://genius.com/zedd-the-middle-lyrics'
page=requests.get(URL)
html = BeautifulSoup(page.text, "html.parser")
lyrics = html.find("div", class_="lyrics").get_text()

print(lyrics)