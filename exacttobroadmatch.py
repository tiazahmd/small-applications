#!/usr/bin/python3

# A tool that reads clipboard, takes the exact phrases and
# converts them to broad match modified phrases

import sys
import pyperclip

exactMatches = pyperclip.paste()
exactMatchesSplit = exactMatches.split("\n")

# Getting rid of square braces

for i in range(len(exactMatchesSplit)):
    exactMatchesSplit[i] = exactMatchesSplit[i].replace("[", "")
    exactMatchesSplit[i] = exactMatchesSplit[i].replace("]", "")

# Adding + sign infront of all words

for i in range(len(exactMatchesSplit)):
    exactMatchesSplit[i] = exactMatchesSplit[i].split(" ")
    for j in range(len(exactMatchesSplit[i])):
        exactMatchesSplit[i][j] = "+" + exactMatchesSplit[i][j]
    exactMatchesSplit[i] = " ".join(exactMatchesSplit[i])

broadMatch = "\n".join(exactMatchesSplit)
pyperclip.copy(broadMatch)
