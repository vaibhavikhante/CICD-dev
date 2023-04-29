from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def hello():
    return '<h1>this is my  first call</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/post', methods=["POST"])

def testpost():
     input_json = request.get_json(force=True)
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)
