#!/usr/bin/env python3

# the name of the import matches the file name (minus the .py)
# these two files MUST BE IN THE SAME DIRECTORY
import first_module

# first_module.main() # Executes the main function of first_module

first_module.greeting()

print("Module #2 Name=", __name__)