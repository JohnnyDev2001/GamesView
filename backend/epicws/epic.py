import requests
from bs4 import BeautifulSoup
import json

url = "https://store.epicgames.com/pt-BR/browse?sortBy=releaseDate&sortDir=DESC&category=Game&count=40"

header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Cookie":"EPIC_LOCALE_COOKIE=pt-BR; _epicSID=19d943a5700f43ce811aae0888db9ca9; __cf_bm=HCE97RHU9k2N5KBj9H4BG9.BOgL6gcMP.9fyRk.LM2M-1656277829-0-AT9CLj12tjsbVkiFVGAzXXzI/pDXHLqce5RflIwKT9MNwksL+w13FpNNF7tj5kLkw08pV5JofBdMC2HjYD34KViz4Fo0YgJlVFZV6a2pMQ4FZtGAiuT19ckTpBH4nJ+ny3drEAewj8bkosdajwUvwfdqqXCVR1tDIZx1Q1qiQK+8",
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