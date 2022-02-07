from flask import Flask
from flask_cors import CORS

from api.model import db
from api.controller.hello_controller import hello_api
from api.controller.carts_controller import cart_api
from api.controller.product_controller import product_api


def create_app(config_filename):
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.register_blueprint(hello_api)
    app.register_blueprint(cart_api)
    app.register_blueprint(product_api)
    db.init_app(app)
    CORS(app)

    return app
