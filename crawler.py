from bs4 import BeautifulSoup
import requests

url = requests.get("https://myanimelist.net/anime/season")
mal_web_page = url.content

soup = BeautifulSoup(mal_web_page, "lxml")

for i in soup.find_all('h2', {'class':'h2_anime_title'}):
    link = i.find('a', href=True)
    if link is None:
        continue
    print(link['href'])