from flask import request, Response, redirect
from flask import Flask
from flask import render_template
from flask import url_for
import json

app = Flask("ble_discovery")
app.run(host='0.0.0.0',debug=True)

statusFilePath = "static/status.json"
facesNb = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


#http://172.18.0.2:5000/static/devices.json
@app.route('/devices')
def send():
    return "<a href=%s>file</a>" % url_for('static', filename='devices.json')

@app.route('/getfaces')
def getFaces():
    f = open(statusFilePath, "r")
    faces =  f.read()
    return str(faces)

# http://127.0.0.1:5003/setfaces?faces=2
@app.route('/setfaces', methods=['GET'])
def setFaces():
    with open(statusFilePath,'w') as f: 
        pass
    f.close()
    args = request.args
    facesNb = args
    jsonDump = json.dumps(facesNb)
    f = open(statusFilePath, "a")
    f.write(str(jsonDump))
    return args