import time
import data_importer
import data_exporter
import datetime

debug_mode = False
RSI_codes = {
    0 : "Overbought",
    1 : "Neutral",
    2 : "Oversold",
    3 : "Data Error: Bad Header",
    4 : "Data Error: Bad Data Body",
    5 : "Data Error: API Call Rate Exceeded"
}
MOM_codes = {
    0 : "Negative",
    1 : "Neutral",
    2 : "Positive",
    3 : "Data Error: Bad Header",
    4 : "Data Error: Bad Data Body",
    5 : "Data Error: API Call Rate Exceeded"
}

RSI_trigger_oversold = 30
RSI_trigger_overbought = 70
sleep_time = 25

#TODO clean up main.py... some of these functions make sense to belong to their own module
#TODO add logging and error handling
#TODO clean up according to PEP8
#TODO add option of calling functions with custom settings and storing defaults in an easily accesable config file
#TODO add CLI


def RSI_checker(ticker):


    # Return Code Key
    # 0 = overbought
    # 1 = neutral
    # 2 = oversold
    # 3 = Data Error: Bad Header
    # 4 = Data Error: Bad Data Body
    # 5 = Data Error: API Call Rate Exceeded
    try:
        historical_data = data_importer.request_RSI(str(ticker))
        if historical_data == {"Information": "Thank you for using Alpha Vantage! Please visit https://www.alphavantage.co/premium/ if you would like to have a higher API call volume."}:
            return 5
        historical_data = (historical_data['Technical Analysis: RSI'])
    except KeyError:
        return 3
    output_file= []
    working_file = {}
    counter = 1
    for item in historical_data:
        working_file[counter] = historical_data[item]
        output_file.append(working_file[counter])
        counter += 1
    try:
        if debug_mode:
            print(output_file[1]['RSI'])
        if float(output_file[1]['RSI']) <= RSI_trigger_oversold:
            return 2
        elif float(output_file[1]['RSI']) >= RSI_trigger_overbought:
            return 0
        else:
            return 1
    except IndexError:
        return 4


def MOM_checker(ticker):


    # Return Code Key
    # 0 = Negative
    # 1 = Neutral
    # 2 = Positive
    # 3 = Data Error: Bad Header
    # 4 = Data Error: Bad Data Body
    # 5 = Data Error: API Call Rate Exceeded
    try:
        # TODO refactor variable name... historical_data does not make much sense
        historical_data = data_importer.request_MOM(str(ticker))
        if historical_data == {"Information": "Thank you for using Alpha Vantage! Please visit https://www.alphavantage.co/premium/ if you would like to have a higher API call volume."}:
            return 5
        historical_data = (historical_data['Technical Analysis: MOM'])
    except KeyError:
        return 3
    output_file= []
    working_file = {}
    counter = 1
    for item in historical_data:
        working_file[counter] = historical_data[item]
        output_file.append(working_file[counter])
        counter += 1
    try:
        if debug_mode:
            print(output_file[1]['MOM'])
        if float(output_file[1]['MOM']) > 0:
            return 2
        elif float(output_file[1]['MOM']) < 0:
            return 0
        elif float(output_file[1]['MOM']) == 0:
            return 1
    except IndexError:
        return 4


def check_watchlist():
    start_time = time.time()
    counter = 0
    output_list = [["TICK", 'MOM', 'RSI']]
    ticker_list = data_importer.import_watchlist()
    estimate_time = round(len(ticker_list) * sleep_time / 60)
    print('{} {}'.format(estimate_time, ' minutes expected runtime'))
    for stock in ticker_list:
        MOM_status = MOM_checker(stock)
        RSI_status = RSI_checker(stock)
        output_item = [stock, MOM_codes[MOM_status], RSI_codes[RSI_status]]
        output_list.append(output_item)
        if MOM_status and RSI_status == 2:
            print('{} {}'.format(stock, ' is a candidate!'))
        else:
            if debug_mode:
                print('{} {} {} {} {}'.format(stock, 'MOM ', MOM_status, ' | RSI ', RSI_status))
        counter += 1
        if counter % 25 == 0:
            print('{} {}'.format(counter, ' stocks have been checked.'))
        time.sleep(sleep_time)
    data_exporter.to_CSV(output_list, "RSI and Momentum Daily Checkup")
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_minutes = elapsed_time // 60
    elapsed_time_seconds = round(elapsed_time % 60)
    print('{} {} {} {} {} {} {}'.format('Processing completed on ', counter, ' equities in ', elapsed_time_minutes, ' minutes and ', elapsed_time_seconds, ' seconds.'))


check_watchlist()