from flask import Blueprint

from .product import product_bp
from .functionality import functionality_bp
from .customer import customer_bp
from .order import order_bp

def register_routes(app):
    app.register_blueprint(product_bp)
    app.register_blueprint(functionality_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(order_bp)
