def hexToBin(hexa):
    binForHex = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', 
                '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                 'E': '1110', 'F': '1111', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101',
                 'e': '1110', 'f': '1111'}
    
    hexaBroken = list(hexa)

    finalBin = ""

    for i in range(len(hexaBroken)):
        finalBin = finalBin + binForHex[hexaBroken[i]]

    return finalBin

def binToDec(binaryData):
    base64 = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K',
                '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U',
                '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': 'a', '27': 'b', '28': 'c', '29': 'd', '30': 'e', 
                '31': 'f', '32': 'g', '33': 'h', '34': 'i', '35': 'j', '36': 'k', '37': 'l', '38': 'm', '39': 'n', '40': 'o',
                '41': 'p', '42': 'q', '43': 'r', '44': 's', '45': 't', '46': 'u', '47': 'v', '48': 'w', '49': 'x', 
                '50': 'y', '51': 'z', '52': '0', '53': '1', '54': '2', '55': '3', '56': '4', '57': '5', '58': '6', '59': '7',
                '60': '8', '61': '9', '62': '+', '63': '/',}

    # Check if the binary data size is multiple of 6
    if len(binaryData) % 6 == 0:
        pass
    else:
        temp = 6 - (len(binaryData) % 6)
        for i in range(0, temp, 1):
            binaryData[i] = "0" + binaryData[i]

    # Check if the first 6 integers are all 0 or not
    for i in range(len(binaryData)):
        if binaryData[0:6] == '000000':
            binaryData = binaryData[6:]
        else:
            pass    
    
    # Binary to decimal
    multipleOfSix = int(len(binaryData) / 6)
    bin6array = []
    low = 0
    high = 6
    for i in range(0, multipleOfSix):
        bin6array.append(binaryData[low:high])
        low += 6
        high += 6

    decArray = []

    for i in range(len(bin6array)):
        dec = 0
        for digits in bin6array[i]:
            dec = (dec * 2) + int(digits)
        decArray.append(str(dec))
    
    # Decimal to Base64
    baseChar = []
    for items in decArray:
        baseChar.append(base64[items])

    baseFinal = "".join(baseChar)

    print(baseFinal)
    
binToDec(hexToBin('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))