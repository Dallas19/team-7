from flask import Flask, request, Response, send_from_directory, send_file
from flask_cors import CORS
import os.path
import csv

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/getInterviewSchedule', methods=['POST'])
def interviewScheduler():
    #file = request.files['StudentInput_Example']
    for file in request.files.getlist('files'):
            file.save(os.path.join(download, secure_filename(file.name)))
    return 'success'
    #return app.send_static_file("server/testFiles/CompanyInput_Blank.csv")
    #return str(files)

@app.route('/getOfferMatches')
def offerMatches():
    return "getOfferMatches"
