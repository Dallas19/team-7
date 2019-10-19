# importing csv module
import csv



class CSVParser:


    def parseStudentFile(filename):
        # initializing the titles and rows list
        fields = []
        rows = []

        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = csvreader.next()

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))
        # printing the field names
        print('Field names are:' + ', '.join(field for field in fields))
        #  printing first 5 rows
        print('\nFirst 5 rows are:\n')
        for row in rows[:5]:
            # parsing each column of a row
            for col in row:
                print("%10s" % col),
            print('\n')
        pass

    def parseStudentFile(filename):
        # initializing the titles and rows list
        fields = []
        rows = []

        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = csvreader.next()

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))
        # printing the field names
        print('Field names are:' + ', '.join(field for field in fields))
        #  printing first 5 rows
        print('\nFirst 5 rows are:\n')
        for row in rows[:5]:
            # parsing each column of a row
            for col in row:
                print("%10s" % col),
            print('\n')
        pass


def __main__():
    # csv file name
    filename = "TestFiles/StudentInput_Example.csv"
    CSVParser.parseStudentFile(filename)




