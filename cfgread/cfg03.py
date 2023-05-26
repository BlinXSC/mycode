#!/usr/bin/env python3

file_name = input("Please provide the name of the file to be read >>> ")

## create file object in "r"ead mode
with open(file_name, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    print(len(configlist))

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
