import requests
from bs4 import BeautifulSoup
import json

url = "https://store.epicgames.com/pt-BR/browse?sortBy=releaseDate&sortDir=DESC&category=Game&count=40"

header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Cookie":"EPIC_LOCALE_COOKIE=pt-BR; _epicSID=19d943a5700f43ce811aae0888db9ca9; __cf_bm=tuF924uvayPPdqg0GLAtonFzriDYW44swnPkP7qasIc-1656280192-0-ASPEA92NgOVtKK0jEh0hTkhYmgdZufFtWO+OcczYPRewJyaDLRKP1FjAy8XTuoPlK5HOm4N5O3fJ7b1zl2ruspIt+3p03AakLTqcvNFBDDyUNG7Z7HO08pINoSdK4EElvybOGufeTNCKFCTyTq2AFvM5eTo9L0M6mxT5m574z7rf",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
}

html = requests.get(url, headers=header)
soup = BeautifulSoup(html.text, 'html.parser')

def get_games():
    gameList = []
    games = soup.find_all('a', {'class': 'css-15fmxgh'})

    for game in games: 
        titulo = game.find('div', {'class': 'css-1h2ruwl'}).text
        
        try:
            price = game.find('div', {'class': 'css-4jky3p'}).text.strip().split()
        except:
            price = ""
        
        try:
            promo = game.find('span', {'class': 'css-z3vg5b'}).text.strip().split()
        except:
            promo = ""

        try:
            porcent_promo = game.find('div', {'class': 'css-l24hbj'}).text.strip().split()
        except:
            porcent_promo = ""

        imgLink = game.find('img')['data-image']
        l = {
            'title': titulo,
            'price': [price, promo, porcent_promo],
            'imgLink': imgLink
        }
        gameList.append(l)

    return gameList

def Export_Spider(lista):
    lista = list(lista)
    return json.dumps(lista)
    

lista = get_games()
epic = Export_Spider(lista)

print(epic)