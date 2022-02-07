from datetime import datetime
from email import contentmanager
from flask import request
from flask import jsonify
from flask import json
from flask import Blueprint

from api.model import db
from api.model.cart_model import Cart
from api.service import cart_service

cart_api = Blueprint('carts', __name__)


@cart_api.route("/carts/")
@cart_api.route("/carts/<cart_code>")
def get(cart_code=None):
    """Lista todos ou exibe os detalhes de um cart quando cart_code informado."""
    if cart_code is not None:
        return jsonify(cart_service.get_by_code(cart_code).serialized)
    else:
        carts = cart_service.get_all_carts()
        return jsonify({
            'carts': [c.serialized for c in carts]
        })


@cart_api.route("/carts/<cart_code>", methods=['PUT'])
def put(cart_code=None):
    """Atualiza um cart a partir da lista de produtos enviada no payload."""
    payload = request.get_json()
    saved = cart_service.save_content(cart_code, payload)

    return jsonify(saved.serialized)
