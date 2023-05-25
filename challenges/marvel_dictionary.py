#!/usr/bin/env python3

# Prompts the user to provide a character they want to know more about.
char_name = input("Which character do you want to know more about? (Starlord, Mystique, Hulk) >>> ")
char_stat = input("What statistic do you want to know more about? (real name, powers, archenemy) >>> ")

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}")