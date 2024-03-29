from flask import Flask, Response, send_from_directory, send_from_directory
from flask_cors import CORS
from flask import render_template, request, redirect, url_for
from werkzeug import secure_filename
import os
import csv
from Algorithm import Algorithm

app = Flask(__name__, static_url_path='')
CORS(app)
app.config['UPLOAD_FOLDER'] = "app.instance_path/download"
    #return app.send_static_file("server/testFiles/CompanyInput_Blank.csv")
    #return str(files)
@app.route('/getInterviewSchedule', methods=['POST'])
def interviewScheduler():
    #file = request.files['StudentInput_Example']
    #print(dir(request), flush=True)
    #print(request.__dict__, flush=True)
    #prinnt(request.files, flush=True)
    #prent(request.files['student'], flush=True)
    filenameList = []
    for file in (request.files['student'], request.files['company']):
        filenameList.append('download/' + file.filename)
        p = os.path.join(app.root_path, 'download/' + file.filename)
        file.save(p)
        print(p, flush=True) # debug

    # call to Algorithm file
    if len(filenameList) >= 2:
        studentFilename = filenameList[0]
        companyFilename = filenameList[1]
        algorithm = Algorithm(studentFilename, companyFilename)
        
        # file deletion
        os.remove(filenameList[0])
        os.remove(filenameList[1])
    return "success"
        
@app.route('/getOfferMatches', methods=['GET'])
def offerMatches():
    file = open('./matchResults/offerMatchings.csv', 'r')
    returnfile = file.read().encode('latin-1')
    file.close()
    return Response(returnfile, mimetype="text/csv", headers = {"Content-disposition": 
    "attachment; filename=offerMatchings.csv"})
   
@app.route('/getInterviewMatch', methods=['GET'])
def download():
    return send_from_directory('matchResults', filename='offerMatchings.csv')
    

    #file = request.files['file']
    #file.save(os.path.join(app.root_path, 'download/file.csv'))
    
    #file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
