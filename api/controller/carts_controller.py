from datetime import datetime
from flask import request
from flask import jsonify
from flask import json
from flask import Blueprint

from api.model import db
from api.model.cart_model import Cart

cart_api = Blueprint('carts', __name__)


@cart_api.route("/carts/")
@cart_api.route("/carts/<cart_code>")
def get(cart_code=None):
    """Lista todos ou exibe os detalhes de um cart quando cart_code informado."""
    if cart_code is not None:
        cart = Cart.query.filter(
            Cart.code == cart_code
        ).one()
        return jsonify(cart.serialized)
    else:
        carts = Cart.query.all()
        return jsonify({
            'carts': [c.serialized for c in carts]
        })


@cart_api.route("/carts/<cart_code>", methods=['PUT'])
def put(cart_code=None):
    """Atualiza um cart a partir da lista de produtos enviada no payload."""
    payload = request.get_json()

    Cart.query.filter(Cart.code == cart_code).update(
        {
            Cart.content: json.dumps(payload),
            Cart.updated_at: datetime.utcnow()
        }, synchronize_session=False
    )
    db.session.commit()

    return jsonify(Cart.query.filter(Cart.code == cart_code).one().serialized)
