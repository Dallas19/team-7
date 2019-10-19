from flask import Flask, request, Response
from flask_cors import CORS
import os.path


app = Flask(__name__)
CORS(app)

@app.route('/getInterviewSchedule', methods=['POST'])
def interviewScheduler():
    #file = request.files['StudentInput_Example']
    #files = request.files.getlist('files[]')
    #print(files[0])
    path = "server/testFiles/CompanyInput_Blank.csv"
    return app.send_static_file(path)


@app.route('/getOfferMatches')
def offerMatches():
  path = "server/testFiles/CompanyInput_Blank.csv"
  return app.send_static_file(path)

def get_file(filename):  # pragma: no cover
    try:
        src = filename
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)

class File:
  def __init__(self, name):
    self.name = name
