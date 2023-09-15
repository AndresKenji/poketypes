import sys, argparse
from pokeactions import get_pokemons_by_region, get_pokemons_by_type


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action',
                        type=str,
                        help="Indica el tipo de acción que deseas realizar:\n\ttype: Genera una grafica segun el numero de pokemons por tipo \n\tregion: Genera una grafica segun el numero de pokemons por region")
    args = parser.parse_args()
    action(args.action)
    
def action(action):
    if action == "type":
        print("Obteniendo pokemones por tipo")
        get_pokemons_by_type()
        
    if action == "region":
        print("Obteniendo pokemones por region")
        get_pokemons_by_region()   

if __name__ == "__main__":
    main()