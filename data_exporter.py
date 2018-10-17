import csv
import datetime


def name_builder(symbol, date, report_type):
    return str(symbol) + '_' + str(report_type) + '_' + date + '.csv'


# takes a dictionary with symbol, report_type, report date, field_one_name, and field_two_name data as a header and any two other fields as main data and generates a simple report in csv format
# def to_CSV(report):
#     dictionary = report
#     symbol = dictionary['symbol']
#     report_type = dictionary['report_type']
#     report_date = dictionary['report_date']
#     file_name = str(symbol) + '_' + str(report_type) + '_' + report_date + '.csv'
#     field_one_name = dictionary['field_one_name']
#     field_two_name = dictionary['field_two_name']
#     del dictionary['symbol']
#     del dictionary['report_type']
#     del dictionary['report_date']
#     del dictionary['field_one_name']
#     del dictionary['field_two_name']
#     output_list = []
#     output_list.append([str(field_one_name) , str(field_two_name)])
#     for item in dictionary:
#         output_list.append([str(item), str(dictionary[item])])
#     with open(file_name, 'w+', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         for line in output_list:
#             writer.writerow(line)

def to_CSV(report_list, report_title):
    report_date = str(datetime.date.today())
    file_name = str(report_title) + '_' + report_date + '.csv'
    with open(file_name, 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in report_list:
            writer.writerow(line)
