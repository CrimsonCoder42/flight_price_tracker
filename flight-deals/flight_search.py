import os
import requests
from dotenv import load_dotenv
load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API = os.getenv("TEQUILA_API")


class FlightSearch:
    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "apikey": TEQUILA_API,
        }

    def get_destination_code(self, city_name):
        tequila_data = requests.get(TEQUILA_ENDPOINT, headers=self.headers, params={"term": f"{city_name}", "location_types": "city"})
        data = tequila_data.json()
        return data["locations"][0]["code"]

