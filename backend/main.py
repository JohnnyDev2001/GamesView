from flask import Flask
app = Flask(__name__)

from epicws.epic import epic
from steamws.steam import steam

@app.route('/')
def index():
    return epic, steam

@app.route('/steam')
def OnlySteam():
    return steam

@app.route('/epic')
def OnlyEpic():
    return epic