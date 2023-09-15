import requests

URL_BASE = "https://pokeapi.co/api/v2/"


def get_pokemons(limit:int=1000):
    end_point = f"pokemon?limit={limit}"
    url = URL_BASE + end_point
    try:
        response = requests.get(url).json()
        return response
    except Exception as e:
        return str(e)
    
def get_regions():
    url = URL_BASE + 'region'
    try:
        response = requests.get(url).json()
        return response
    except Exception as e:
        print(e)
        return 'Error'

def get_pokemons_region(region_url:str):
    try:
        response = requests.get(region_url)
        region_data = response.json()
        pokedex = requests.get(region_data['pokedexes'][0]['url']).json()

        return pokedex['pokemon_entries']
    except Exception as e:
        print(e)
        return 'Error'