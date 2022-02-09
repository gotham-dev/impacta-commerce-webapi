
from flask import Blueprint
from flask import jsonify
from datetime import datetime

hello_api = Blueprint('hello', __name__)


@hello_api.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@hello_api.route("/timestamps", methods=['GET'])
def get():
    return jsonify({
        'now': datetime.utcnow().isoformat(),
    })
