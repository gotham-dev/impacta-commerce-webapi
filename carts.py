from datetime import datetime
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import json

# Inicializa a aplicação Flask com configurações padrão
app = Flask(__name__)
CORS(app)

# Inicializa a conexão com um banco de dados SQLite em memória.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db = SQLAlchemy(app)


class Cart(db.Model):
    """Cria a entidade de Cart"""
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, unique=False, nullable=False)
    updated_at = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return '<Cart %r>' % self.title

    @property
    def serialized(self):
        return {
            'id': self.id,
            'code':  self.code,
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat(),
            'products': json.loads(self.content),
        }


# Cria o banco de dados em memória
db.create_all()

# Cria um Cart inicial de acordo com o protótipo.
now = datetime.utcnow()
cart_products = """
[
  {
    "code": "1",
    "title": "Caneca Personalizada de Porcelana",
    "tumbnailUrl": "http://meu-ecommerce.com/img/pr/tb-pers-porc.jpg",
    "qty": 1,
    "unitPrice": 123.45
  },
  {
    "code": "2",
    "title": "Caneca Importada Personalizada em Diversas Cores",
    "tumbnailUrl": "http://meu-ecommerce.com/img/pr/tb-import-colors.jpg",
    "qty": 2,
    "unitPrice": 123.45
  },
  {
    "code": "3",
    "title": "Caneca de Tulipa",
    "tumbnailUrl": "http://meu-ecommerce.com/img/pr/tb-tuli.jpg",
    "qty": 1,
    "unitPrice": 123.45
  }
]
"""
cart = Cart(code="fixed-cart-code", content=cart_products,
            created_at=now, updated_at=now)

json.loads(cart_products)

# Insere os dois produtos no banco de dados em memória
db.session.add(cart)

# Commit a transaction do banco de dados.
db.session.commit()


@app.route("/carts/")
@app.route("/carts/<cart_code>")
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


@app.route("/carts/<cart_code>", methods=['PUT'])
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
