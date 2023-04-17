import requests
import json


def buscando_pokemon(idPokemon):

    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    busqueda = requests.get(url_api + idPokemon)
    if busqueda.status_code == 200:
        pokemon = json.loads(busqueda.content)
        print("pokemon encontrado:" + pokemon['name'])
        print("peso " + str(pokemon['weight']) + " gramos")
        print("altura " + str(pokemon['height']))
    else:
        print("pokemon no encontrado, verifique el id ingresado")

def tipos(idPokemon):
    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    busqueda = requests.get(url_api + idPokemon)
    if busqueda.status_code == 200:
        pokemon = json.loads(busqueda.content)
        for name in pokemon['types']:
            print("tipo de pokemons: ", name)

def main():
    idPokemon = input("ingrese el id del pokemo")
    buscando_pokemon(idPokemon)
    tipos(idPokemon)
main()