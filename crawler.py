from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

def info_anime(soup, output):
    output = []

    #Extracting the name of the anime

    anime=soup.find(name="h1",attrs={"class":"title-name h1_bold_none"})
    name=anime.text
    output.append(name)

    # japan=soup.find(name="span",attrs={"class":"dark_text"})
    # japanese=japan.text
    # print ("Japanese Title: "+japanese)

    #Extracting the rating

    rating=soup.find(name="div",attrs={"class":"fl-l score"})
    output.append((rating.text.strip()))


    #extracting the description

    des=soup.find(name="p",attrs={"itemprop":"description"})
    description=des.text
    output.append(description)

    #Extracting the Rank

    rank=soup.find(name="span",attrs={"class":"numbers ranked"})
    output.append(rank.text)

    #Extracting number of episodes

    ep=soup.find(name="div",attrs={"class":"spaceit"})
    output.append(ep.text)

    return output

    # print (info_anime(soup))

url = requests.get("https://myanimelist.net/anime/season")
mal_web_page = url.content

soup = BeautifulSoup(mal_web_page, "lxml")

names = []
ratings = []
descriptions = []
ranks = []
num_episodes = []

for i in soup.find_all('h2', {'class':'h2_anime_title'}):
    anime_links_queue = []

    link = i.find('a', href=True)
    if link is None:
        continue

    anime_links_queue.append(link['href'])

    output = ""

    url = requests.get(anime_links_queue.pop(0))
    anime_info_page = url.content
    soup_info = BeautifulSoup(anime_info_page, "html.parser")
    out = info_anime(soup_info, output)

    names.append(out[0])
    ratings.append(out[1])
    descriptions.append(out[2])
    ranks.append(out[3])
    num_episodes.append(out[4])

    time.sleep(60)

df = pd.DataFrame({
        'name': names,
        'rating': ratings,
        'description': descriptions,
        'rank': ranks,
        'num_episodes': num_episodes,
        'timestamp': "2021-06-10"
})

df.to_csv('output.csv', index=False)