from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    #return 'Hello, World!'
    response = ""
    term = request.args['term']
    if term:
        items = [ "c++", "java", "php", "coldfusion", "javascript", "asp", "ruby", "perl", "ocaml", "haskell", "rust", "go" ]
        response = jsonify([item for item in items if item.startswith(term)])
        response.headers.add('Access-Control-Allow-Origin', '*')
    return response