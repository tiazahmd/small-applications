from hextobin import hexToBin

def binToDec(binaryData):
    # Check if the binary data size is multiple of 6
    if len(binaryData) % 6 == 0:
        pass
    else:
        temp = 6 - (len(binaryData) % 6)
        for i in range(0, temp, 1):
            binaryData = "0" + binaryData

    # Check if the first 6 integers are all 0 or not
    for i in range(len(binaryData)):
        if binaryData[0:6] == '000000':
            binaryData = binaryData[6:]
        else:
            pass    
    
    # Convert binary to decimal
    decData = 0
    initial = 1
    for i in range(len(binaryData) - 1, 0, -1):
        decData = decData + (int(binaryData[i]) * initial)
        initial = initial * 2
    print(binaryData)
    print(decData)

binToDec(hexToBin('9F2'))