from flask import Blueprint, request, jsonify
from models import db, Order
from schemas import OrderSchema

order_bp = Blueprint('order', __name__)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

@order_bp.route('/order', methods=['POST'])
def add_order():
    customer_id = request.json['customer_id']
    amount = request.json['amount']
    product_id = request.json['product_id']

    new_order = Order(customer_id, amount, product_id)
    db.session.add(new_order)
    db.session.commit()

    return order_schema.jsonify(new_order)

@order_bp.route('/order', methods=['GET'])
def get_orders():
    all_orders = Order.query.all()
    result = orders_schema.dump(all_orders)
    return jsonify(result)

@order_bp.route('/order/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return order_schema.jsonify(order)

@order_bp.route('/order/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get_or_404(id)
    order.customer_id = request.json['customer_id']
    order.amount = request.json['amount']
    order.product_id = request.json['product_id']

    db.session.commit()
    return order_schema.jsonify(order)

@order_bp.route('/order/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()

    return order_schema.jsonify(order)
