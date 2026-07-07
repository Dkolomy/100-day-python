import requests

api_key = "c8160754d5d29113a0adb577da567186"
lat = 42.765366
lon = -71.473842

# https://api.openweathermap.org/data/4.0/forecast?lat=42.765366&lon=-71.4738424&appid=c8160754d5d29113a0adb577da567186
url = f"https://api.openweathermap.org/data/4.0/onecall/current?lat={lat}&lon={lon}&appid={api_key}"
# response = requests.get(url)
# data = response.json()
# print(data)

# https://api.openweathermap.org/data/4.0/onecall/current?lat=42.765366&lon=-71.4738424&units=metric&lang=en&appid=c8160754d5d29113a0adb577da567186

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall/forecast"
params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
data = response.json()
print(data["list"][0]["weather"][0]["id"] )

will_rain = False
for item in data["list"]:
  condition_code = item["weather"][0]["id"]
  if condition_code < 700:
    will_rain = True

if will_rain:
  print("Bring an umbrella")  
