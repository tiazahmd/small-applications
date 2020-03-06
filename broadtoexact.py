#!/usr/bin/python3

# A tool that reads clipboard, takes the broad match modified phrases and
# converts them to exact match phrases

import sys
import pyperclip

broadMatches = pyperclip.paste()
broadMatchesSplit = broadMatches.split("\n")

def broadToExact(broadMatchesSplit):
    for i in range(len(broadMatchesSplit)):
        broadMatchesSplit[i] = "[" + broadMatchesSplit[i] + "]"
    exactMatch = "\n".join(broadMatchesSplit)
    pyperclip.copy(exactMatch)

broadToExact(broadMatchesSplit)
