import xlrd
import csv
from os import sys

def csv_from_excel(excel_file, csv_path):

    wb = xlrd.open_workbook(excel_file)
    # wb.sheet_by_index(0)
    sh = wb.sheet_by_name('Manhours')
    your_csv_file = open(csv_path + excel_file.split('.')[0] + '.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Required paramters 1. Path of excel file \n 2. Location to save the CSV file")
    csv_from_excel(sys.argv[1], sys.argv[2])
