from xml.sax.handler import all_properties
from flask import request
from flask import Blueprint
from flask import jsonify
from api.service import product_service

product_api = Blueprint('products', __name__)


@product_api.route("/products", methods=['GET'])
def get_products():
    """Cria uma rota para consulta de produtos baseada no parâmetro query."""
    args = request.args.to_dict()
    query = args.get("query")

    all_products = product_service.get_by_query(query)

    return jsonify({
        'query': query,
        'size': 10,
        'start': 'MA==',
        'results': [p.serialized for p in all_products]
    })
