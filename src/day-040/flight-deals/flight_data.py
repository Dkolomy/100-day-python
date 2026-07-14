import requests

class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

    def find_cheapest_flight(data, return_date):
        # Handle empty data if no flight data is returned
        if data is None or (not data.get("best_flights") and not data.get("other_flights")):
            print("No flight data found")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

        # Combine best_flights and other_flights into a single list
        all_flights = data.get("best_flights", []) + data.get("other_flights", [])
        
        # Data from the first flight in the list
        first_flight = all_flights[0]
        lowest_price = first_flight["price"]
        origin = first_flight["flights"][0]["departure_airport"]["id"]
        destination = first_flight["flights"][-1]["arrival_airport"]["id"]
        out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

        # A fliht with 2 segments will have 1 stop
        nr_stops = len(first_flight["flights"]) - 1

        # Initialize FlightData with the first flight for comparizon
        cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)

        for flight in all_flights:
            # Exception handling - json has data but flight is missing 'price'. Skip.
            try:
                price = flight["price"]
            except KeyError:
                print("Flight missing 'price' data. Skipping.")
                continue

            if price < lowest_price:
                lowest_price = price
                origin = flight["flights"][0]["departure_airport"]["id"]
                destination = flight["flights"][-1]["arrival_airport"]["id"]
                out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
                nr_stops = len(flight["flights"]) - 1
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)
                print(f"New cheapest flight found: {cheapest_flight.price} from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} on {cheapest_flight.out_date}")

        return cheapest_flight
                    
    # def get_flight_data(self, city_name):
    #     response = requests.get(f"https://api.tequila.kiwi.com/v2/search?apikey={TEQUILA_API_KEY}&term={city_name}")
    #     response.raise_for_status()
    #     self.flight_data = response.json()
    #     return self.flight_data