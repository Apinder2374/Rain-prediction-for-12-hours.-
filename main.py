import requests 
from twilio.rest import Client
import os 
import sys

OMW_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "47d534d32cb79c15c0e627ce3ebee159"

parameters = {
    "lat":28.644800,
    "lon": 77.216721,
    "cnt":4,
    "appid": api_key
}

account_sid = "AC6cdd70db9a75e4f657dddb59aeddcde7"
auth_token = "52664beda8983ebe097c48ed7bdb3651"

response = requests.get(OMW_endpoint, params=parameters)
data = response.json()

will_rain = False
for items in data["list"]:
    temps = items["main"]["temp"]
    if temps < 700:
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body = 'It might rain today!☂️',
            from_ = '+15136438662',
            to = '+919582548338'
        )
    print(message.status)
