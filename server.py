from flask import Flask, jsonify,request, session, redirect
from tinydb import TinyDB,Query
app = Flask(__name__)
# app.secret_key = "ola"

db = TinyDB("test.json")

@app.route('/data',methods=['POST','GET'])
def get_data():
    if request.method == 'GET':
        if "snake" in session:
            pos = session["snake"]
            print(pos)
            # return str(pos)
            return db.all()
        else:
            content = db.all()
            print(type(content))
            return content
            # return "No snake"
    elif request.method == 'POST':
        data = request.json
        session["snake"] = data["snake"]
        return redirect("http://127.0.0.1:5000/data")

@app.route('/api',methods=['POST','GET'])
def get_req():
    if request.method == 'POST':
        data = request.json
        session["key1"] = data["key1"]
        # aux = data["key1"]
        resposnse_data = {'received data': data}

        return jsonify(resposnse_data),200
    if request.method == 'GET':
        return 'Deu para receber o GET'
    else:
        return 'Invalid request method',405

@app.route('/show',methods = ['GET'])
def show():
    if request.method == 'GET':
        # data = request.json
        # resposnse_data = {'received data': data}
        return 
    
    else:
        return 'Não deu para fazer a magia acontecer'
if __name__ == '__main__':
    app.run()