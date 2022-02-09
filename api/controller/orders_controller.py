from flask import Blueprint, request
from api.service import order_service
from flask import jsonify

order_api = Blueprint('orders', __name__)


@order_api.route("/orders/")
@order_api.route("/orders/<order_id>")
def get(order_id=None):
    """Lista todos
     ou exibe os detalhes de um cart quando cart_code informado."""

    if order_id is not None:
        return jsonify(order_service.get_by_id(order_id).serialized)
    else:
        return jsonify({
            'orders': [o.serialized for o in order_service.get_all()]
        })


@order_api.route("/orders/", methods=['POST'])
def post():
    """Cria um pedido, a partir de um código de Cart informado."""
    payload = request.get_json()
    cart_code = payload["cart_code"]

    order = order_service.create_from(cart_code)

    return jsonify(order.serialized)
