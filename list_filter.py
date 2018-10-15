import csv

with open('companylist.csv', newline='') as my_csv_file:
    csv_reader = csv.reader(my_csv_file)
    next(csv_reader, None)
    for row in csv_reader:
        try:
            if float(row[2]) <= 25 and float(row[3]) > 1000000000:
                print(row[0])
        except:
            pass