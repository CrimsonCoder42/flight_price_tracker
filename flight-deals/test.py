import json
from pprint import pprint
from flight_search import FlightSearch


flight_search = FlightSearch()
data = flight_search.get_destination_code("Paris")



def get_iata_code(num):
    codes = []
    for location in num['locations']:
        if 'code' in location:
            codes.append(location['code'])
    print(codes)

get_iata_code(data)

# # Open the JSON file
# with open('data.json') as json_file:
#     data = json.load(json_file)
#     locations = data['locations']
#     airports = [location['id'] for location in locations]
#
# # Now the file has been read into the `data` variable and you can work with it as a normal dictionary
# print(airports)

