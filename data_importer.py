import requests
import json
url_part_one = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
url_part_two='&apikey='
API_key = 'EQUA0WMPJLI4A9SQ'


def request_builder(symbol):
    url = str(url_part_one) + str(symbol) + str(url_part_two) + str(API_key)
    r = requests.get(url)
    return r.json()

