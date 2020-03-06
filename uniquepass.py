import random

def passGen(count):

    genPass = []

    # Generating the first 4 mandatory random characters

    genPass.extend(chr(random.randint(65, 90))) # Generating chars from A-Z
    genPass.extend(chr(random.randint(97, 122))) # Generating chars from a-z
    genPass.extend(chr(random.randint(48, 57))) # Generating numbers from 0-9
    genPass.extend(chr(random.randint(33, 47))) # Generating special chars

    remCount = count - 4

    # Generating (if) remaining characters

    for i in range(0, remCount):
        randomNumber = random.randint(0,3)

        if randomNumber == 0:
            genPass.extend(chr(random.randint(65, 90)))
        elif randomNumber == 1:
            genPass.extend(chr(random.randint(97, 122)))
        elif randomNumber == 2:
            genPass.extend(chr(random.randint(48, 57)))
        else:
            genPass.extend(chr(random.randint(33, 47)))

    # Shuffling the characters

    for i in range(0,9):
        randomOne = random.randint(0, count-1)
        randomTwo = random.randint(0, count-1)
        genPass[randomOne], genPass[randomTwo] = genPass[randomTwo], genPass[randomOne]

    return ''.join(genPass)

# Validation

while True:
    try:
        passCount = int(input('Enter how many characters of password you need (at least 4): '))
        if passCount < 4:
            print('Password needs to be at least 4 characters long.')
        else:
            break
    except ValueError:
        print('Please enter only integers.')

print('Your unique password is: ' + passGen(passCount))
