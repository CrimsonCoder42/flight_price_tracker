import os
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData


SHEETY_ENDPOINT = "https://api.sheety.co/55aa9079fb5635ff903fe1909e3652fd/flightDeals/sheet1"
data_manager = DataManager()
sheet_data = data_manager.get_sheety_data()


if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
else:
    from flight_data import FlightData
    flight_data = FlightData()
    for row in sheet_data:
        all_options = flight_data.get_flight_data(row["iataCode"])
        if all_options["data"][0]["price"] < row["lowestPrice"]:
            print("Low price alert!")
            print(f"Low price alert! Only £{all_options['data'][0]['price']} to fly from {all_options['data'][0]['cityFrom']}-{all_options['data'][0]['flyFrom']} to {all_options['data'][0]['cityTo']}-{all_options['data'][0]['flyTo']}, from {all_options['data'][0]['route'][0]['local_departure']} to {all_options['data'][0]['route'][1]['local_departure']}")
            print(f"https://www.google.co.uk/flights?hl=en#flt={all_options['data'][0]['flyFrom']}.{all_options['data'][0]['flyTo']}.{all_options['data'][0]['route'][0]['local_departure']}*{all_options['data'][0]['flyTo']}.{all_options['data'][0]['flyFrom']}.{all_options['data'][0]['route'][1]['local_departure']}")
        print("it is here", all_options)





#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


