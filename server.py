from flask import Flask, jsonify,request, session

app = Flask(__name__)
aux = ""
@app.route('/data')
def get_data():
    data = {'message': f'{snake.positions}'}
    return jsonify(data)

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