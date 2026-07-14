import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
# SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/your_username/flightDeals/prices"


class DataManager:
    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.user_endpoint = os.environ["SHEETY_USER_ENDPOINT"]
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        response.raise_for_status()
        data = response.json()
        # print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    # ==================== Updated the price in the spreadsheet ====================
        
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

    def get_customer_emails(self):
       response = requests.get(url=self.users_endpoint, auth=self._authorization)
       response.raise_for_status()
       data = response.json()
       self.customer_data = data["users"]
       return self.customer_data
