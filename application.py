import os
from flask import *
from flask_wtf import FlaskForm

from jinja2 import Environment, PackageLoader, select_autoescape
from datetime import *
import re
import json
import db  # if error, right-click parent directory "mark directory as" "sources root"
import time


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPER SECRET SKELINGTON'


# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_time_from_seconds(seconds):
    minutes = "{:02.0f}".format(seconds/60)
    seconds = "{:06.3f}".format(seconds%60)
    timeStr  = minutes + ":" +seconds
    return timeStr

def get_seconds_from_time(time):
    minutes = time[0:2]
    seconds = time[3:5]
    milis = time[7:11]
    newTime = (int(minutes)*60) + int(seconds) + (int(milis)/1000)
    return newTime

# Various Form classes

@app.before_request
def before_request():
    #db.open_db_connection()
    pass


@app.teardown_request
def teardown_request(exception):
    #db.close_db_connection()
    pass


@app.route('/', methods=['GET','POST'])
def index():
    print("Home page")
    return render_template('index.html')

@app.route('/council_results', methods=['GET','POST'])
def council_results():
    return render_template('council_results.html')

@app.route('/algo_benchmark', methods=['GET','POST'])
def algo_benchmark():
    
    return render_template('algo_benchmark.html',modes= 1, GBmodes = 2, algoNames = 3)



@app.context_processor
def test_debug():

    def console_log(input_1,  input_2 = '', input_3 = ''):
        print("logging", input_1)
        print(input_2)
        print(input_3)
        return input_1
    

    return dict(log=console_log)



# ---------TODO: Get SSL context ssl_context=('/etc/letsencrypt/live/tuschedulealerts.com/fullchain.pem', '/etc/letsencrypt/live/tuschedulealerts.com/privkey.pem'----------------------------------
if '__main__' == __name__:
    #app.run(host='0.0.0.0', port=5000, debug=True) 
    app.run( host='0.0.0.0',port=5001, debug=True)
