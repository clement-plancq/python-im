from flask import Flask, jsonify
import json

examples = json.load(open("examples.json"))

app = Flask(__name__)

@app.route('/<verb>')
def hello_world(verb):
    
    if verb in examples:
        res = examples[verb]
    else:
        res = ""
    #return 'Hello World!'
    #return Response(json.dumps(res),  mimetype='application/json')
    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response    

if __name__ == '__main__':
    app.run()
