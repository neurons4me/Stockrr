import requests

def request_time_series_daily(symbol):
    url_part_one = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    url_part_two = '&apikey='
    API_key = 'EQUA0WMPJLI4A9SQ'
    url = str(url_part_one) + str(symbol) + str(url_part_two) + str(API_key)
    r = requests.get(url)
    return r.json()

def request_time_series_daily_long(symbol):
    url_part_one = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    url_part_two = '&outputsize=full&apikey='
    API_key = 'EQUA0WMPJLI4A9SQ'
    url = str(url_part_one) + str(symbol) + str(url_part_two) + str(API_key)
    r = requests.get(url)
    return r.json()

def request_RSI(symbol):
    url_part_one = 'https://www.alphavantage.co/query?function=RSI&symbol='
    url_part_two = '&interval=60min&time_period=100&series_type=close&apikey='
    API_key = 'EQUA0WMPJLI4A9SQ'
    url = str(url_part_one) + str(symbol) + str(url_part_two) + str(API_key)
    r = requests.get(url)
    return r.json()

def request_MOM(symbol):
    url_part_one = 'https://www.alphavantage.co/query?function=MOM&symbol='
    url_part_two = '&interval=60min&time_period=100&series_type=close&apikey='
    API_key = 'EQUA0WMPJLI4A9SQ'
    url = str(url_part_one) + str(symbol) + str(url_part_two) + str(API_key)
    r = requests.get(url)
    return r.json()