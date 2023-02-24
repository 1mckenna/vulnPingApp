# ping.py
from flask import Flask, render_template, request
import os

app = Flask(__name__)

def do_ping(strIP):
   stream = os.popen('ping -c 4 '+strIP)
   pingResult = stream.read()
   return {"result": pingResult.replace("\n","<br>")}

@app.route("/")
def ping():
    return render_template('ping.html')

@app.route('/ping', methods=['POST'])
def conCheck():
    ipAddr = request.form['ip']
    result = do_ping(ipAddr)
    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
