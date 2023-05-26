#!/usr/bin/env python3

count = 0

# Use with function to keep file open until completion
with open("dracula.txt") as spooky_file: 
    
    with open ("vampytimes.txt", "w") as outfile:
    
        for line in spooky_file:
            if "vampire" in line.lower():
                print(line)
                count += 1
                outfile.write(line)

print(f"Vampire appears {count} times")