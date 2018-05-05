#!/usr/bin/python3

# A script that saves a copied text with a keyword

import pyperclip, shelve, sys

# Function: Save copied text and keyword
def saveWord(keyword, content):
    shelfFile = shelve.open('myCopiedList')
    shelfFile[keyword] = content
    print("Copied text saved. Keyword: " + keyword + ". Copied text: " + content)
    shelfFile.close()

# Function: Shows the list of copied items on the file
def showList():
    shelfFile = shelve.open('myCopiedList')
    shelfList = list(shelfFile)
    for i in range(len(shelfList)):
        print(shelfList[i] + ": " + shelfFile[shelfList[i]])
    shelfFile.close()

# Function: Extracting copied text with a keyword
def extractWord(keyword):
    shelfFile = shelve.open('myCopiedList')
    try:
        extractedWord = shelfFile[keyword]
        pyperclip.copy(extractedWord)
        print("Copied: " + extractedWord)
    except KeyError:
        print("Keyword doesn't exist")

# Function: Deleting keyword-copied text group
def deleteWord(keyword):
    shelfFile = shelve.open('myCopiedList')
    del shelfFile[keyword]
    print("Deleted keyword: " + keyword)

# Function: Shows manual on how to use the tool
def showManual():
    print("To save a copied word: './copysave.py save *keyword*'")
    print("To extract a copied word: './copysave.py ext *keyword*'")
    print("To delete a copied word: './copysave.py del *keyword*'")
    print("To see a list of all copied words with keywords: './copysave.py list'")

# System arguments
if (len(sys.argv) < 2) or (len(sys.argv)) > 3:
    print("Usage: ./copysave.py [command] [keyword]")
    sys.exit()
elif ((len(sys.argv)) == 2) and (sys.argv[1] == "list"):
    showList()
    sys.exit()
elif ((len(sys.argv)) == 2) and (sys.argv[1] == "man"):
    showManual()
    sys.exit()
elif ((len(sys.argv)) == 3) and (sys.argv[1] == "save"):
    keyWord = sys.argv[2]
    content = pyperclip.paste()
    saveWord(keyWord, content)
    sys.exit()
elif ((len(sys.argv)) == 3) and (sys.argv[1] == "ext"):
    keyWord = sys.argv[2]
    extractWord(keyWord)
    sys.exit()
elif ((len(sys.argv)) == 3) and (sys.argv[1] == "del"):
    keyWord = sys.argv[2]
    deleteWord(keyWord)
    sys.exit()
else:
    print("Wrong Usage. Type './copysave.py man' for manual")
