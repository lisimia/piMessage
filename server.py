from flask import Flask
from flask import jsonify
from flask import request
import json
from piMessage import piMessage
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/buddies')
def buddies():
    result = []
    for buddy in piMessage.buddies:
        result.append({
            'id': buddy._id,
            'name': buddy.name,
            'handle': buddy.handle
        })

    return jsonify({'buddies': result})


@app.route('/new', methods=['POST'])
def new():
    print request.form['text']
    print "FROM", request.form['handle']
    return "OK"


@app.route('/send', methods=['POST'])
def send():
    text = request.form['text']
    #find out who id is
    id = request.form['id']
    for buddy in piMessage.buddies:
        if buddy._id == id:
            print text
            print "TO",  buddy.name
            piMessage.send(text, buddy)
            return "SENT"
    else:
        print "NO BUDDY MATCHED", id
        return "ERROR", 404



if __name__ == '__main__':
    app.run()
