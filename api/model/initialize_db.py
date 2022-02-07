from api.model import db
from flask import json
from datetime import datetime
from api.model.cart_model import Cart
from api.model.product_model import Product

def init():
    # Cria o banco de dados em memória
    db.create_all()

    init_carts()
    init_products()

def init_carts():
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


def init_products():
    # Cria dois produtos
    product1 = Product(
        title='Caneca Personalizada de Porcelana', amount=123.45,
        installments=3, installments_fee=False)

    product2 = Product(
        title='Caneca de Tulipa', amount=123.45,
        installments=3, installments_fee=False)

    # Insere os dois produtos no banco de dados em memória
    db.session.add(product1)
    db.session.add(product2)

    # Commit a transaction do banco de dados.
    db.session.commit()