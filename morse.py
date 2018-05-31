#! /usr/bin/python3.6

# Morse code: https://morsecode.scphillips.com/morse2.html

morseDict = {'A':'.- ', 'B':'-... ', 'C':'-.-. ', 'D':'-.. ',
            'E':'. ', 'F': '..-. ', 'G':'--. ', 'H':'.... ',
            'I':'.. ', 'J':'.--- ', 'K':'-.- ', 'L':'.-.. ',
            'M':'-- ', 'N':'-. ', 'O':'--- ', 'P':'.--. ',
            'Q':'--.- ', 'R':'.-. ', 'S':'... ', 'T':'- ',
            'U':'..- ', 'V':'...- ', 'W':'.-- ', 'X':'-..- ',
            'Y':'-.-- ', 'Z':'--.. ', '0':'----- ', '1':'.---- ', 
            '2':'..--- ', '3':'...-- ', '4':'....- ', 
            '5':'..... ', '6':'-.... ', '7':'--... ',
            '8':'---.. ', '9':'----. ', '.': '.-.-.- ',
            ',':'--..-- ', '?':'..--.. ', ':':'---... ', 
            '\'':'.----. ', '-':'-....- ', '/':'-..-. ',
            '(':'-.--.- ', ')':'-.--.- ', '"':'.-..-. ',
            '@':'.--.-. ', '=':'-...- ', " ":'/ '}

def userChoice():
    print("---Morse Code Translator---")
    print("What do you want to do?")
    print("1. Translate English to Morse Code")
    print("2. Translate Morse Code to English")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        englishString = input("Enter English String: ")
        englishToMorse(englishString)
    elif choice == "2":
        morseString = input("Enter Morse Code String: ")
        morseToEnglish(morseString)
    elif choice == "3":
        return False
    else:
        print("Please choose either 1, 2 or 3.\n")

def englishToMorse(englishString):
    morseEngList = list(englishString)
    morseCodeList = []
    for chars in morseEngList:
        morseCodeList.append(morseDict[chars])
    finalMorseCode = "".join(morseCodeList)
    print("\n" + finalMorseCode + "\n")

def morseToEnglish(morseString):
    morseCodeList = list(morseString.split(" "))
    morseMod = [item + " " for item in morseCodeList]
    englishList = []
    for chars in morseMod:
        for key, values in morseDict.items():
            if values == chars:
                englishList.append(key)
    finalEnglish = "".join(englishList)
    print("\n" + finalEnglish + "\n")

while True:
    if userChoice() == False:
        break