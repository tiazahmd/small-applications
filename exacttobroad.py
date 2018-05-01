#!/usr/bin/python3

# A tool that reads clipboard, takes the exact phrases and
# converts them to broad phrases

import sys
import pyperclip

exactMatches = pyperclip.paste()
exactMatchesSplit = exactMatches.split("\n")

# Getting rid of square braces

for i in range(len(exactMatchesSplit)):
    exactMatchesSplit[i] = exactMatchesSplit[i].replace("[", "")
    exactMatchesSplit[i] = exactMatchesSplit[i].replace("]", "")

broadMatch = "\n".join(exactMatchesSplit)
pyperclip.copy(broadMatch)
