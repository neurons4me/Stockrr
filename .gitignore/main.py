import data_importer
import data_exporter
import datetime
import time

#ticker = input('Enter Ticker Symbol')
#do some inputr validation here

#TODO make an import function to import a list from file to perfrom a batch
ticker_list = ['AAPL', 'GOOG', 'OGEN', 'CHK','TWTR', 'IGC']

def volatility(ticker):
    historical_data = data_importer.request_builder(str(ticker))
    historical_data = (historical_data['Time Series (Daily)'])
    output_file = {'symbol':ticker, 'report_date': str(datetime.date.today()), 'report_type': 'volatility', 'field_one_name': 'Date', 'field_two_name': 'Volatility % (Daily mean / Day High - Day Low)'}
    for day in historical_data:
        day_data = historical_data[day]

        variance_range = float(day_data['2. high']) - float(day_data['3. low'])
        variance_average =  (float(day_data['2. high']) + float(day_data['3. low'])) / 2
        variance_percent = (variance_range / variance_average) *100


        output_file[day] = variance_percent
    return output_file

#TODO put inside a fucntion, add logging and error handling
for symbol in ticker_list:
    data_exporter.to_CSV(volatility(symbol))
    time.sleep(15)


