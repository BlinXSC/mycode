#!/usr/bin/env python3

import requests
import shutil
import json

def main():
    # practice slicing from API

    # pick a pokemon ID number
    pokenum= input("Pick a number between 1 and 151!\n> ")

    # retrive api
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # part 1
    print(pokeapi['sprites']['front_default'])
    res = requests.get(pokeapi['sprites']['front_default'], stream = True)

    if res.status_code == 200:
        with open(f"/home/student/mycode/challenges/pokemon_API/{pokeapi['name']}.png",'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded:', f"/home/student/mycode/challenges/pokemon_API/{pokeapi['name']}.png")
    else:
        print('Image Couldn\'t be retrieved')

    # part 2
    """
    for x in pokeapi['moves']:
        print(x['move']['name'])
    """

    # part 3
    # print(len((pokeapi['game_indices']))) # no for loop

    count = 0
    for x in pokeapi['game_indices']:
        count += 1

    print(f"{pokeapi['name'].capitalize()} appears in {count} games")

main()
