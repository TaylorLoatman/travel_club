import security
import requests


class FlightSearch:
    """
    FlightSearch class has 2 functions to help user find flight deals
    find_code finds user departure and arrival city code.
    flight search takes users form input and outputs flight information
    """

    def __init__(self):
        self.endpoint = security.flight_search_endpoint
        self.key = security.flight_key
        self.header = security.flight_header

    def find_code(self, city_name):

        data_params = {
            'term': city_name,
            'location_types': 'city',
                }

        location_endpoint = f"{self.endpoint}/locations/query"

        response = requests.get(url=location_endpoint, params=data_params, headers=self.header)
        results = response.json()['locations'][0]['code']
        return results

    def flight_information(self, from_location, to_location, start_date, to_date):
        locate_endpoint = f"{self.endpoint}/v2/search"

        params = {
            'fly_from': from_location,
            'fly_to': to_location,
            'date_from': start_date,
            'date_to': to_date,
            'flight_type': 'oneway',
            'curr': 'USD',
            'limit': '3'
        }

        response = requests.get(url=locate_endpoint, params=params, headers=self.header)

        dep_city = response.json()['data'][0]['cityFrom']
        dep_code = response.json()['data'][0]['cityCodeFrom']
        arrival_city = response.json()['data'][0]['cityTo']
        arrival_code = response.json()['data'][0]['cityCodeTo']
        price_1 = response.json()['data'][0]['price']
        travel_country = response.json()['data'][0]['countryTo']['name']
        purchase_link_1 = response.json()['data'][0]['deep_link']
        outbound_date_1 = response.json()['data'][0]['route'][0]['local_departure'].split('T')[0]

        price_2 = response.json()['data'][1]['price']
        purchase_link_2 = response.json()['data'][1]['deep_link']
        outbound_date_2 = response.json()['data'][1]['route'][0]['local_departure'].split('T')[0]

        price_3 = response.json()['data'][2]['price']
        purchase_link_3 = response.json()['data'][2]['deep_link']
        outbound_date_3 = response.json()['data'][2]['route'][0]['local_departure'].split('T')[0]

        flight_data_txt = {
            'dep_city': dep_city,
            'dep_code': dep_code,
            'arrival_city': arrival_city,
            'arrival_code': arrival_code,
            'price': [price_1, price_2, price_3],
            'outbound_date': [outbound_date_1, outbound_date_2, outbound_date_3],
            'country_code': travel_country,
            'purchase_link': [purchase_link_1, purchase_link_2, purchase_link_3],
        }

        return flight_data_txt
