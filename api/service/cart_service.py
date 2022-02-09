from api.model.cart_model import Cart
from flask import json
from datetime import datetime
from api.model import db
from api.model import initialize_db


def get_by_code(cart_code):
    cart = Cart.query.filter(
        Cart.code == cart_code
    ).first()

    if cart is None:
        initialize_db.init_carts()
        db.session.commit()
        return get_by_code(cart_code)

    return cart


def get_all_carts():
    return Cart.query.all()


def save_content(cart_code, content):
    Cart.query.filter(Cart.code == cart_code).update(
        {
            Cart.content: json.dumps(content),
            Cart.updated_at: datetime.utcnow()
        }, synchronize_session=False
    )
    db.session.commit()

    return get_by_code(cart_code)


