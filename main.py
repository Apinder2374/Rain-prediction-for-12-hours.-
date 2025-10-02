import requests 
from twilio.rest import Client
import os 


OMW_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv('OWN_API_KEY')

parameters = {
    "lat":os.getenv('LAT'),
    "lon":os.getenv('LON'),
    "cnt":os.getenv('CNT'),
    "appid": api_key
}

account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

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
            from_ = os.getenv('TWILIO_FROM'),
            to = os.getenv('TWILIO_TO')
        )
    print(message.status)
