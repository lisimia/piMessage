from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/new', methods=['POST'])
def new():
    print request.form['text']
    print "FROM", request.form['handle']
    return "OK"

if __name__ == '__main__':
    app.run()

