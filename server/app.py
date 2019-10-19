from flask import Flask, request
app = Flask(__name__)

@app.route('/getInterviewSchedule', methods=['POST'])
def interviewScheduler():
    #file = request.files['StudentInput_Example']
    files = request.files.getlist('files[]')
    return files

@app.route('/getOfferMatches')
def offerMatches():
  return 'OfferMatches'


class File:
  def __init__(self, name):
    self.name = name
