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

    def performAlgorithm(self):
        offered = False
        first_student_requeue = -1 # assume student id is positive
        current_queue_length = -1 # placeholder values

        while not self.studentQueue:
            student_id = self.studentQueue.popleft()
            wanted = set()
            for job_id in self.jobsRankingDict: # creating wanted[] this student
                go_to_next_job = False
                if not self.jobsRankingDict[job_id]:
                    continue
                # self.jobsRankingDict[job_id][0] is top student for job
                while self.jobsRankingDict[job_id][0] in self.students_with_offers: # check for existing students
                    self.jobsRankingDict[job_id] = self.jobsRankingDict[job_id][1:]
                    if not self.jobsRankingDict[job_id]:
                        go_to_next_job = True
                        break
                if go_to_next_job:
                    continue
                if self.jobsRankingDict[job_id][0] == student_id: # if top student for job is my next student
                    wanted.add(self.jobsRankingDict[job_id][0])
            
            for job_id in self.studentRankingDict[student_id]:
                if job_id in wanted:
                    self.result.append((job_id, student_id))
                    offered = True
                    self.numPositionsDict[job_id] -= 1
                    self.students_with_offers.add(student_id)
                    break
            
            if not offered:
                if current_queue_length == len(self.studentQueue) + 1 and first_student_requeue == student_id:
                    break
                self.studentQueue.append(student_id)
                current_queue_length = len(self.studentQueue)
                first_student_requeue = student_id
                
        open_positions = sum([self.numPositionsDict[job_id] for job_id in self.numPositionsDict])

        for job_id in self.jobsRankingDict:
            go_to_next_job = False
            if not self.jobsRankingDict[job_id]:
                continue
            while self.jobsRankingDict[job_id][0] in self.students_with_offers: # check for existing students
                self.jobsRankingDict[job_id] = self.jobsRankingDict[job_id][1:]
                if not self.jobsRankingDict[job_id]:
                    go_to_next_job = True
                    break
            if go_to_next_job:
                continue
            if self.numPositionsDict[job_id] > 0:
                self.result.append((job_id, self.jobsRankingDict[job_id][0])) # add the top student for that job
                open_positions -= 1
                self.numPositionsDict[job_id] -= 1
                self.students_with_offers.add(self.jobsRankingDict[job_id][0])
            if open_positions == 0:
                break

    def __init__(self, studentFilePath, companyFilePath):
        self.studentRows = CSVParser.parseStudentFile(studentFilePath)
        self.companyRows = CSVParser.parseCompanyFile(companyFilePath)

        self.studentQueue = collections.deque()
        self.studentRankingDict = {}
        self.jobsRankingDict = {}
        self.numPositionsDict = {}

        self.populateDataStructures()

        self.result = []
        self.students_with_offers = set()
        self.performAlgorithm()

        print(self.result)

        #print("Printing studentQueue")
        #print(self.studentQueue)
        #print("\nPrinting studentRanking")
        #print(self.studentRankingDict)
        #print("\nPrinting jobRanking")
        #print(self.jobsRankingDict)
        #print("\nPrinting numPositions")
        #print(self.numPositionsDict)

if __name__ == "__main__":
    studentFilename = "testFiles\\StudentInput_Example.csv"
    companyFilename = "testFiles\\CompanyInput_Example.csv"
    algorithm = Algorithm(studentFilename, companyFilename)
    pass