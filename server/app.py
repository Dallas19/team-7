from flask import Flask, Response, send_from_directory, send_file
from flask_cors import CORS
from flask import render_template, request, redirect, url_for
from werkzeug import secure_filename
import os
import csv

app = Flask(__name__, static_url_path='')
CORS(app)
app.config['UPLOAD_FOLDER'] = "app.instance_path/download"


    #return app.send_static_file("server/testFiles/CompanyInput_Blank.csv")
    #return str(files)
@app.route('/getInterviewSchedule', methods=['POST'])
def interviewScheduler():
    #file = request.files['StudentInput_Example']
    for file in request.files.getlist('files'):
        file.save(os.path.join(app.root_path, 'download/' + file.filename))
    return "success"


@app.route('/getOfferMatches', methods=['POST'])
def offerMatches():
    file = request.files['file']
    file.save(os.path.join(app.root_path, 'download/file.csv'))
    return "getOfferMatches"
    #file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
