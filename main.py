import requests
import json

lista = []

def buscando_pokemon(idPokemon):

    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    busqueda = requests.get(url_api + idPokemon)
    if busqueda.status_code == 200:
        pokemon = json.loads(busqueda.content)
        print("pokemon encontrado:" + pokemon['name'])
        print("peso " + str(pokemon['weight']) + " gramos")


    else:
        print("pokemon no encontrado, verifique el id ingresado")

def tipo(idPokemon):
    global lista
    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    busqueda = requests.get(url_api + idPokemon)
    if busqueda.status_code == 200:
        lista.append(type)
        print(lista[:])



def main():
    idPokemon = input("ingrese el id del pokemo")
    buscando_pokemon(idPokemon)
    tipo(idPokemon)
main()