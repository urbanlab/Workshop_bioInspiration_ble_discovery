from flask import request, Response, redirect
from flask import Flask
from flask import render_template
from flask import url_for

app = Flask("inventaire")
app.run(host='0.0.0.0',debug=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


#http://172.18.0.2:5000/static/devices.json
@app.route('/devices')
def send():
    return "<a href=%s>file</a>" % url_for('static', filename='devices.json')
