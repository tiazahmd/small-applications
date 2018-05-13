#! /usr/bin/python3

import requests, json
import datetime
import smtplib

currentResponse = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=84101&units=imperial&APPID=bf2733da19f7cb43b2c1c8b2b02ee9bf')
currentData = currentResponse.json()
forecastResponse = requests.get('https://api.openweathermap.org/data/2.5/forecast?zip=84101&units=imperial&APPID=bf2733da19f7cb43b2c1c8b2b02ee9bf')
forecastData = forecastResponse.json()

fullBody = '''
    Current weather in {city} is:
    Temperature: {currentTemp}F. The highest today will be {highTemp}F
    and the lowest today will be {lowTemp}F.
    Weather pattern today mostly: {descriptionC}\n
    Here's the next 5 days' forecast:
'''.format(city = currentData['name'],
            currentTemp = str(currentData['main']['temp']),
            highTemp = str(currentData['main']['temp_max']),
            lowTemp = str(currentData['main']['temp_min']),
            descriptionC = currentData["weather"][0]['main']
            )
for i in range(len(forecastData['list'])):
    bodyForecast = '''
    Date: {date} | Max Temp: {maxTemp}F | Min Temp: {minTemp}F
    Description: {descriptionF}
    '''.format(date = str(datetime.datetime.fromtimestamp(int(forecastData['list'][i]['dt'])).strftime('%a %H:%M:%S ')),
                maxTemp = str(forecastData['list'][i]['main']['temp_max']),
                minTemp = str(forecastData['list'][i]['main']['temp_min']),
                descriptionF = forecastData['list'][i]['weather'][0]['main']
                )
    fullBody = fullBody + bodyForecast

emailTo = "imtiaz.ahmed.ratul@gmail.com"
emailFrom = "ratul.bad@gmail.com"
# emailPass = Google App Password
emailSubject = "Today's Weather Report"
emailBody = fullBody

emailObj = smtplib.SMTP('smtp.gmail.com', 587) # Establishing connection to the gmail client.
emailObj.ehlo() # Always do this. It makes sure that it's connected. Otherwise the followiing codes won't work.
emailObj.starttls() # Start TLS encryption, if using any other port except 465. I'm using 587, therefore initiating TLS.
emailObj.login(emailFrom, emailPass) # Login to email.

emailObj.sendmail(emailFrom, emailTo, "Subject: {subject}\n{body}".format(subject = emailSubject, body = fullBody)) # Send the email.

emailObj.quit() # Always do this to quit the SMTP connection.
