from flask import Flask
app = Flask(__name__)

@app.route('/getInterviewSchedule')
def interviewScheduler():
  return 'interviewScheduler'

@app.route('/getOfferMatches')
def offerMatches():
  return 'OfferMatches'
