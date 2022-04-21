from urllib import response
import requests as r


def getpokedata(pokemon):
    pokemon = pokemon.lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = r.get(url)
    pokedata = response.json()
    return pokedata

class Pokemon:
    def __init__(self, pokedata):
        print('CLASS INIT')
        self.sprite = pokedata['sprites']['front_default']
        self.name = pokedata['name']
        self.hp = pokedata['stats'][0]['base_stat']
        self.attack = pokedata['stats'][1]['base_stat']
        self.defense = pokedata['stats'][2]['base_stat']
