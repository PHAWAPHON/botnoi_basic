from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


url = "https://jsonplaceholder.typicode.com"


@app.route('/')
def home():
    return "Hello World"
    
#API POSTรับ JSON body
@app.route('/posts', methods=['POST'])
def post_api():
    data = request.get_json()
    print(data)
    return jsonify(data),200
#API POSTรับ param
@app.route('/param', methods=['POST'])
def post_param_api():
    param_value = request.args
    jsonify(param_value)
    print(param_value.to_dict())
    return jsonify({'param_name': param_value}),200

#API POSTรับ datafrom
@app.route('/dataform', methods=['POST'])
def data_form ():
    data = request.form
    print(data.to_dict())
    return jsonify(data),200

#API POSTรับ header
@app.route('/header', methods=['POST'])
def header_endpoint():
    header_value = request.headers
    print(header_value)
    return jsonify(200),200

#API GET
@app.route('/body', methods=['GET'])
def header_body():
    data = url+"/posts"
    test_data = requests.get(data).json()
    return jsonify(test_data),200


if __name__ == "__main__":
    app.run(debug=True)
