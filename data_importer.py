import requests
import csv


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
    url_part_two = '&interval=daily&time_period=100&series_type=close&apikey='
    API_key = 'EQUA0WMPJLI4A9SQ'
    url = str(url_part_one) + str(symbol) + str(url_part_two) + str(API_key)
    r = requests.get(url)
    return r.json()


def request_MOM(symbol):
    url_part_one = 'https://www.alphavantage.co/query?function=MOM&symbol='
    url_part_two = '&interval=daily&time_period=100&series_type=close&apikey='
    API_key = 'EQUA0WMPJLI4A9SQ'
    url = str(url_part_one) + str(symbol) + str(url_part_two) + str(API_key)
    r = requests.get(url)
    return r.json()


def import_watchlist():
    with open('watchlist.txt') as watchlist:
        lines = watchlist.readlines()
        output_list = []
        for line in lines:
            currentline = line.rstrip()
            output_list.append(currentline)
        return output_list


def import_portfolio():
    with open('portfolio.csv', newline='') as my_csv_file:
        csv_reader = csv.reader(my_csv_file)
        output_list = []
        for row in csv_reader:
            output_list.append(row)
    return output_list


def request_IEX_price(stock):
    url = 'https://api.iextrading.com/1.0/stock/' + str(stock) + '/price'
    r = requests.get(url)
    return r.json()
