from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from index import init


app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def index():
   
    return jsonify("Hello fucking world")
    
    
@app.route("/teste", methods=['GET'])
def upload():
  
  result_data = init()
  
  return jsonify(result_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
