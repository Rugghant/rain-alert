import os
import requests
from twilio.rest import Client

OWM_Endpoint ="https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 43.6532,
    "lon": -79.3832,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data["list"][1]["weather"][0]["id"]

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today! take an umbrella☂️",
        from_=os.environ.get|("FROM_PH"),
        to=os.environ.get("TO_PH")
    )
    print(message.status)

# print(data["list"][1]["weather"][0]["description"])