import requests
from bs4 import BeautifulSoup
import json

url = "https://store.steampowered.com/search"

html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

def get_games():
    gameList = []
    games = soup.find_all('a', attrs={"class": "search_result_row"})

    for game in games:
        titulo = game.find('span', {'class': 'title'}).text
        price = game.find('div', {'class': 'search_price'}).text.strip().split("R$")
        imgLink = game.find('img')['src']

        l = {
            'title': titulo,
            'price': price,
            'imgLink': imgLink
        }
        gameList.append(l)

    return gameList

def Export_Spider(lista):
    lista = list(lista)
    return json.dumps(lista)
    

lista = get_games()
steam = Export_Spider(lista)