from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

from epicws.epic import epic
from steamws.steam import steam

@app.route('/')
def index():
    both = epic, steam
    return both

@app.route('/steam')
def OnlySteam():
    return steam

@app.route('/epic')
def OnlyEpic():
    return epic