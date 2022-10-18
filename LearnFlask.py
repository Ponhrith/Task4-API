from flask import Flask, jsonify, request, send_file
app = Flask(__name__)

@app.route('/my-first-api', method = ['GET'])

def hello():
    name = request.args.get('name')

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello' + name + '!'

    return jsonify({"message": text})




if __name__ == '__main__':
    app.run(debug=True, port=8000)