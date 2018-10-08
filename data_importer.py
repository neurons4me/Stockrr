import requests

def request_time_series_daily(symbol):
    url_part_one = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    url_part_two = '&apikey='
    API_key = 'EQUA0WMPJLI4A9SQ'
    url = str(url_part_one) + str(symbol) + str(url_part_two) + str(API_key)
    r = requests.get(url)
    return r.json()

def request_time_series_daily(symbol):
    url_part_one = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    url_part_two = '&apikey='
    API_key = 'EQUA0WMPJLI4A9SQ'
    url = str(url_part_one) + str(symbol) + str(url_part_two) + str(API_key)
    r = requests.get(url)
    return r.json()