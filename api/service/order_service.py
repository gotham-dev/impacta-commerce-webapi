from math import prod
import re
from api.model.cart_model import Cart
from api.model.order_model import Order
from flask import json
from datetime import datetime
from api.model import db
from api.service import cart_service


def get_all():
    return Order.query.all()


def get_by_id(id):
    return Order.query.get(id)


def create_from(cart_code):
    with db.session.begin():
        cart = cart_service.get_by_code(cart_code)
        now = datetime.utcnow()
        order = Order(products=cart.content, total_amount=sum_total(cart.content),
                      created_at=now, updated_at=now, status='DONE')

        db.session.add(order)
        db.session.delete(cart)

        # Commit a transaction do banco de dados.
        db.session.commit()

        return order


def sum_total(products_json):
    products = json.loads(products_json)
    print(products)
    total_amount = 0
    for product in products:
        print(product)
        total_amount += product['qty'] * product['unitPrice']

    return total_amount
