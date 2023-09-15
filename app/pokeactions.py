import matplotlib.pyplot as plt
import requests
from pokeapi_request import get_pokemons, get_pokemons_region, get_regions

def get_pokemons_by_type():
    pokemons = get_pokemons()
    pokemon_count_by_type = {}

    for pokemon in pokemons['results']:
        url = pokemon['url']
        response = requests.get(url)
        pokemon_data = response.json()
        
        for pokemon_type in pokemon_data['types']:
            type_name = pokemon_type['type']['name']
            if type_name in pokemon_count_by_type:
                pokemon_count_by_type[type_name] += 1
            else:
                pokemon_count_by_type[type_name] = 1

    types = list(pokemon_count_by_type.keys())
    counts = list(pokemon_count_by_type.values())

    plt.figure(figsize=(12, 6))
    plt.bar(types, counts, color='skyblue')
    plt.xlabel('Tipos de Pokémon')
    plt.ylabel('Número de Pokémon')
    plt.title('Número de Pokémon por Tipo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def get_pokemons_by_region():
    data = get_regions()
    regions = [(region['name'], region['url']) for region in data['results']]
    types_by_region = {}
    for region_name, region_url in regions:
        num_pokemons = len(get_pokemons_region(region_url))
        types_by_region[region_name] = num_pokemons

    region_names = list(types_by_region.keys())
    num_pokemons = list(types_by_region.values())

    plt.figure(figsize=(12, 6))
    plt.bar(region_names, num_pokemons, color='lightcoral')
    plt.xlabel('Regiones de Pokémon')
    plt.ylabel('Cantidad de Pokémon')
    plt.title('Cantidad de Pokémon por Región')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    