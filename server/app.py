from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getInterviewSchedule', methods=['POST'])
def interviewScheduler():
    #file = request.files['StudentInput_Example']
    files = request.files.getlist('files[]')
    print(files)
    return files

@app.route('/getOfferMatches')
def offerMatches():
  return 'OfferMatches'


class File:
  def __init__(self, name):
    self.name = name
