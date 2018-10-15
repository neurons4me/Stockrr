import data_importer
import data_exporter
import time






#TODO add logging and error handling

def RSI_checker(ticker):
    # 0 = overbought
    # 1 = neutral
    # 2 = oversold
    historical_data = data_importer.request_RSI(str(ticker))
    historical_data = (historical_data['Technical Analysis: RSI'])

    #TODO tie to config file or global var
    RSI_trigger_oversold = 30
    RSI_trigger_overbought = 70
    output_file= []
    working_file = {}
    counter = 1
    for item in historical_data:
        working_file[counter] = historical_data[item]
        output_file.append(working_file[counter])
        counter += 1
    try:
        if float(output_file[1]['RSI']) <= RSI_trigger_oversold:
            return 2
        elif float(output_file[1]['RSI']) >= RSI_trigger_overbought:
            return 0
        else:
            return 1
    except IndexError:
        return 1


def MOM_is_positive(ticker):

    historical_data = data_importer.request_MOM(str(ticker))
    historical_data = (historical_data['Technical Analysis: MOM'])
    output_file= []
    working_file = {}
    counter = 1
    for item in historical_data:
        working_file[counter] = historical_data[item]
        output_file.append(working_file[counter])
        counter += 1
    try:
        if float(output_file[1]['MOM']) > 1:
            return True
        else:
            return False
    except IndexError:
        return False


def check_watchlist():
    counter = 0
    for stock in data_importer.import_watchlist():
        if MOM_is_positive(stock) and RSI_checker(stock) == 2:
            print('{} {}'.format(stock, ' is a candidate!'))
        counter += 1
        if counter % 25 == 0:
            print('{} {}'.format(counter, ' stocks have been checked.'))
        time.sleep(25)


check_watchlist()
#TODO doesnt seem to generate any positives, check to see if something is broken or if there really are no positives, suggest testing on a known positive ticker and checking the output at the MOM and RSI stages to see if that is working