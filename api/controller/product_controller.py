from flask import request
from flask import Blueprint
from flask import jsonify
from api.model.product_model import Product

product_api = Blueprint('products', __name__)


@product_api.route("/products", methods=['GET'])
def get_products():
    """Cria uma rota para consulta de produtos baseada no parâmetro query."""
    args = request.args.to_dict()
    query = args.get("query")

    if query is None:
        all_products = Product.query.all()
    else:
        all_products = Product.query.filter(
            Product.title.like(f'%{query}%')
        ).all()

    return jsonify({
        'query': query,
        'size': 10,
        'start': 'MA==',
        'results': [p.serialized for p in all_products]
    })
