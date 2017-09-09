import random

def passGen(count):
    chars = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
             ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
             ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
             ['!', '@', '#', '$', '%', '&', '?']]

    genPass = []

    # Generating the first 4 mandatory random characters

    genPass.extend(chars[0][random.randint(0,25)])
    genPass.extend(chars[1][random.randint(0,25)])
    genPass.extend(chars[2][random.randint(0,9)])
    genPass.extend(chars[3][random.randint(0,6)])

    remCount = count - 4

    # Generating (if) remaining characters

    for i in range(0, remCount):
        randomNumber = random.randint(0,3)

        if randomNumber == 0 or randomNumber == 1:
            genPass.extend(chars[randomNumber][random.randint(0,25)])
        elif randomNumber == 2:
            genPass.extend(chars[2][random.randint(0,9)])
        else:
            genPass.extend(chars[3][random.randint(0,6)])

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
