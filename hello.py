from flask import Flask
from datetime import datetime
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/timestamps", methods=['GET'])
def get():
    return jsonify({
        'now': datetime.utcnow().isoformat(),
    })