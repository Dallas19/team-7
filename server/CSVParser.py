# importing csv module
import csv
import os
from builtins import staticmethod


class CSVParser:

    #Input:     path\\filename
    #Output:    2D list of strings representing the rows from the student CSV.
    @staticmethod
    def parseStudentFile(filename):
        # initializing the titles and rows list
        fields = []
        rows = []

        cur_path = os.path.dirname(__file__)
        new_path = os.path.relpath(filename, cur_path)
        print(new_path)
        # reading csv file
        with open(new_path, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = csvreader.__next__()

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)
        return rows

    @staticmethod
    #Input:     path\\filename (CSV file)
    #Output:    2D list of strings representing the rows from the CSV.
    def parseCompanyFile(filename):
        # initializing the titles and rows list
        fields = []
        rows = []

        cur_path = os.path.dirname(__file__)
        new_path = os.path.relpath(filename, cur_path)


        # reading csv file
        with open(new_path, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = csvreader.__next__()

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)
        return rows
