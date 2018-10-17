import csv
import data_importer
import requests

# with open('companylist.csv', newline='') as my_csv_file:
#     csv_reader = csv.reader(my_csv_file)
#     next(csv_reader, None)
#     for row in csv_reader:
#         try:
#             if float(row[2]) <= 25 and float(row[3]) > 1000000000:
#                 print(row[0])
#         except:
#             pass

with open('nyse-listed_csv.csv', newline='') as my_csv_file:
    csv_reader = csv.reader(my_csv_file)
    next(csv_reader, None)
    for row in csv_reader:
        try:
            url = 'https://api.iextrading.com/1.0/stock/' + str(row[0]) + '/price'
            r = requests.get(url)
            r = r.json()
            if float(r) < 25:
                print(row[0])
        except:
            pass
