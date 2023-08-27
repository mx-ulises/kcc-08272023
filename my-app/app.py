import os
import time

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'msg': "Hello World!"})

if __name__ == '__main__':
    # Simulate a long startup time
    time.sleep(60)
    # Initialize Flask App
    http_port = int(os.environ.get('HTTP_PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=http_port)

