import os
import requests
from dotenv import load_dotenv
load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_API = os.getenv("TEQUILA_API")

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "apikey": TEQUILA_API,
        }

    def get_flight_data(self, city_name):
        tequila_data = requests.get(TEQUILA_ENDPOINT, headers=self.headers, params={"fly_from": "LON", "fly_to": f"{city_name}", "date_from": "12/09/2023", "date_to": "29/09/2023"})
        data = tequila_data.json()
        return data

