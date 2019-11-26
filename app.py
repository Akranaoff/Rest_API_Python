from flask import Flask, jsonify, request
from dbmodule import insert, select, search


app = Flask(__name__)

@app.route('/register', methods = ['POST'])
def adduser():
    data = request.get_json()
    insert(data['id'],data['password'])
    return jsonify({'message':"Value inserted"})

@app.route('/login', methods = ['POST'])
def check():
    data = request.get_json()
    result = search(data['id'],data['password'])
    if len(result)>0:
        return jsonify({"message" : "logged in"})
    else:
        return jsonify({"message" : "Invalid credentials"})


@app.route('/display')
def displayuser():
    data = request.get_json()
    result = select()
    return jsonify({"Result":result})

app.run(port = 6000)



