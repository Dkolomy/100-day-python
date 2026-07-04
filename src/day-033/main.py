import requests

# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up

API_URL = "http://api.open-notify.org/iss-now.json"
API_URL_SUNSET = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": 51.5074,
    "lng": -0.1278,
    "formatted": 0,
}

response = requests.get(API_URL_SUNSET, params=parameters)
response.raise_for_status()
# print(response.json())

sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]

print(sunrise)
print(sunrise.split("T")[1].split(":")[0])