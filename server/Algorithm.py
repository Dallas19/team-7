from CSVParser import CSVParser
import collections

#     studentFilename = "testFiles\\StudentInput_Example.csv"
#     companyFilename = "testFiles\\CompanyInput_Example.csv"
#     algorithm = Algorithm(studentFilename, companyFilename)
class Algorithm:
    #student csv indexes
    studentIndex = 0
    studentTopJobIndex = 3

    #job csv indexes
    jobIDIndex = 0
    jobNumPositionsIndex = 3
    jobRankingsIndex = 4


    def populateDataStructures(self):
        for row in self.studentRows:
            student = row[Algorithm.studentIndex]

            #Populate student's rankings
            studentRankings = []
            for i in range(Algorithm.studentTopJobIndex, len(row)):
                if row[i] != '':
                    studentRankings.append(row[i])
                else:
                    break

            self.studentQueue.append(student)
            self.studentRankingDict.update( {student : studentRankings})

        for row in self.companyRows:
            jobID = row[Algorithm.jobIDIndex]
            numPositions = row[Algorithm.jobNumPositionsIndex]

            companyRankings = []
            for i in range(Algorithm.jobRankingsIndex, len(row)):
                if row[i] != '':
                    companyRankings.append(row[i])
                else:
                    break

            self.jobsRankingDict.update({jobID : companyRankings})
            self.numPositionsDict.update({jobID : int(numPositions)} )
        pass

    def __init__(self, studentFilePath, companyFilePath):
        self.studentRows = CSVParser.parseStudentFile(studentFilePath)
        self.companyRows = CSVParser.parseCompanyFile(companyFilePath)

        self.studentQueue = collections.deque()
        self.studentRankingDict = {}

        self.jobsRankingDict = {}
        self.numPositionsDict = {}
        self.populateDataStructures()

        #print("Printing studentQueue")
        #print(self.studentQueue)
        #print("\nPrinting studentRanking")
        #print(self.studentRankingDict)
        #print("\nPrinting jobRanking")
        #print(self.jobsRankingDict)
        #print("\nPrinting numPositions")
        #print(self.numPositionsDict)
