from bs4 import BeautifulSoup
import requests
import time

def info_anime(soup, output):

    #Extracting the name of the anime

    anime=soup.find(name="h1",attrs={"class":"title-name h1_bold_none"})
    name=anime.text
    output += "Anime: "+name + "\n"

    # japan=soup.find(name="span",attrs={"class":"dark_text"})
    # japanese=japan.text
    # print ("Japanese Title: "+japanese)

    #Extracting the rating

    rating=soup.find(name="div",attrs={"class":"fl-l score"})
    output += "Rating: "+(rating.text.strip()) + "\n"


    #extracting the description

    des=soup.find(name="p",attrs={"itemprop":"description"})
    description=des.text
    output += "Description : "+description + "\n"

    #Extracting the Rank

    rank=soup.find(name="span",attrs={"class":"numbers ranked"})
    output += rank.text + "\n"

    #Extracting number of episodes

    ep=soup.find(name="div",attrs={"class":"spaceit"})
    output += ep.text + "\n"

    output += "\n"

    return output

    # print (info_anime(soup))

url = requests.get("https://myanimelist.net/anime/season")
mal_web_page = url.content

soup = BeautifulSoup(mal_web_page, "lxml")


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
    with open('output.txt', 'a') as f:
        f.write(out)

    time.sleep(60)