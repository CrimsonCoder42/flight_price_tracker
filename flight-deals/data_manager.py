import requests


SHEETY_ENDPOINT = "https://api.sheety.co/55aa9079fb5635ff903fe1909e3652fd/flightDeals/sheet1"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_sheety_data(self):
        sheety_data = requests.get(SHEETY_ENDPOINT)
        data = sheety_data.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

