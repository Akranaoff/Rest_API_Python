from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name':'dmart',
        'items':[{'name':'chair','price':'100'}]

    }
        ]

@app.route('/All_Stores')
def allstores():
    return jsonify({'result':stores})


@app.route('/Search_store/<string:storename>')
def searchstore(storename):
    for i in stores:
        if i['name']==storename:
            return jsonify(i)

    return jsonify({"message":"store not found"})


@app.route('/addstore', methods = ['POST'])
def addstore():
    data = request.get_json()
    for i in stores:
        if data['name']==i['name']:
            return jsonify({"message":"Store already present"})
    stores.append(data)
    return jsonify({"message":"Store added"})

app.run(port = 6000)

