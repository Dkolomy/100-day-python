#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# https://serpapi.com/google-jobs-api
# API_KEY = "75cab1b66ec8f1c51734f8c74f83b861440d3d1c93e47d122b9e2526b4b376a4"

# import requests_cache
# from dotenv import load_dotenv
# from twilio.rest import Client

import requests_cache
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Conserve requests and preserve your free plan ====================
requests_cache.install_cache(
  "flight_cache",
  urls_expire_after={
    "*.sheety.co*": requests_cache.DO_NOT_CACHE,
    "*": 3600,
  },
)
# ==================== Talk to Sheety ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

pprint(sheet_data)

# ==================== Set the Dates ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# ==================== Do a Flight Search ====================
flight_search = FlightSearch()

notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LHR"

for destination in sheet_data:
  pprint(f"Getting flights for {destination['city']}...")
  flights = flight_search.check_flights(
    ORIGIN_CITY_IATA,
    destination["iataCode"],
    from_time=tomorrow,
    to_time=six_month_from_today
  )
  cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
  pprint(f"Cheapest flight to {destination['city']} found: {cheapest_flight.price}")

  if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
      pprint(f"Lower price flight found to {sheet_data[0]['city']}!")
      data_manager.update_lowest_price(sheet_data[0]["id"], cheapest_flight.price)
      # notification_manager.send_sms(
      #     message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
      #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
      #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
      # )
      # SMS not working? Try whatsapp instead.
      notification_manager.send_whatsapp(
        message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                     f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                     f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
