import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

# SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
# SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/your_username/flightDeals/prices"


class DataManager:
    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        # print(data)
        
    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(f"{SHEETY_PRICES_ENDPOINT}/{row_id}", 
            json=new_data, 
            auth=self._authorization, 
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        print(response.text)

