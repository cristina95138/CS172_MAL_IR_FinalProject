from bs4 import BeautifulSoup
import requests

def info_anime(soup):

    #Extracting the name of the anime

    anime=soup.find(name="h1",attrs={"class":"title-name h1_bold_none"})
    name=anime.text
    print ("Anime: "+name)

    # japan=soup.find(name="span",attrs={"class":"dark_text"})
    # japanese=japan.text
    # print ("Japanese Title: "+japanese)

    #Extracting the rating

    rating=soup.find(name="div",attrs={"class":"fl-l score"})
    print ("Rating: "+(rating.text.strip()))


    #extracting the description

    des=soup.find(name="p",attrs={"itemprop":"description"})
    description=des.text
    print ("Description : "+description)

    #Extracting the Rank

    rank=soup.find(name="span",attrs={"class":"numbers ranked"})
    print (rank.text)

    #Extracting number of episodes

    ep=soup.find(name="div",attrs={"class":"spaceit"})
    print (ep.text)

    # print (info_anime(soup))

url = requests.get("https://myanimelist.net/anime/season")
mal_web_page = url.content

soup = BeautifulSoup(mal_web_page, "lxml")


for i in soup.find_all('h2', {'class':'h2_anime_title'}):
    link = i.find('a', href=True)
    if link is None:
        continue
    url = requests.get(link['href'])
    anime_info_page = url.content
    soup_info = BeautifulSoup(anime_info_page, "html.parser")
    info_anime(soup_info)