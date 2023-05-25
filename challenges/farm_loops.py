#!/usr/bin/env python3

## Part 1
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "marisapig", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

ne_animals = farms[0]["agriculture"]
w_agriculture = farms[1]["agriculture"]
se_agriculture = farms[2]["agriculture"]
barf = ["carrots", "celery"]

for x in ne_animals:
    print(x)

## Part 2 and 3
farm_selection = input("\nPlease select a farm from the following: NE, W, SE >>> ").upper()
farms = ["NE", "W", "SE"]

while farm_selection not in farms:
    print("Invalid input.")
    farm_selection = input("\nPlease select a farm from the following: NE, W, SE >>> ").upper()

if farm_selection == "NE":
    for x in ne_animals:
        if x not in barf:
            print(x)
elif farm_selection == "W":
    for x in w_agriculture:
        if x not in barf:
            print(x)
else:
    for x in se_agriculture:
        if x not in barf:
            print(x)

