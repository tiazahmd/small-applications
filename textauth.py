#! /usr/bin/python3

from twilio.rest import Client
import string, random

# Twilio authentications
accountSID = "AC7880acefc53bf11780991a3193dab825"
authToken = "0e0e82f772358ae6cea3fff1fd928b5b"
twilioClient = Client(accountSID, authToken)

def checkUser(username, password):
    db = {'u': 'admin', 'p':'admin'}
    if username == db['u'] and password == db['p']:
        uAuth()
    else:
        print('Failure')

def uAuth():
    userNumber = "+1" + str(input("Please enter your phone number: "))
    twilioNumber = "+19148734864"
    authCode = generateAuthCode()
    twilioClient.messages.create(body="Your one time authentication code is: " + authCode, 
                                from_=twilioNumber, to=userNumber)
    while True:
        userInputCode = input("Enter the code that was send on your phone: ")
        if userInputCode == authCode:
            print("Success")
            return True
        else:
            print("Wrong code. Try again.")

def generateAuthCode():
    chars = string.ascii_letters + string.digits
    codeLen = 6
    oneTimeCode = ""
    for i in range(codeLen):
        oneTimeCode = oneTimeCode + ''.join((random.choice(chars)))
    return oneTimeCode

def userLogin():
    username = input("Enter username: ")
    password = input("Password: ")
    checkUser(username, password)

userLogin()