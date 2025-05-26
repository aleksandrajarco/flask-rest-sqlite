from flask import Blueprint, request, jsonify
from models import db, Customer
from schemas import CustomerSchema

customer_bp = Blueprint('customer', __name__)

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

@customer_bp.route('/customer', methods=['POST'])
def add_customer():
    name = request.json['name']
    email = request.json['email']

    new_customer = Customer(name, email)
    db.session.add(new_customer)
    db.session.commit()

    return customer_schema.jsonify(new_customer)

@customer_bp.route('/customer', methods=['GET'])
def get_customers():
    all_customers = Customer.query.all()
    result = customers_schema.dump(all_customers)
    return jsonify(result)

@customer_bp.route('/customer/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return customer_schema.jsonify(customer)

@customer_bp.route('/customer/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    customer.name = request.json['name']
    customer.email = request.json['email']

    db.session.commit()
    return customer_schema.jsonify(customer)

@customer_bp.route('/customer/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()

    return customer_schema.jsonify(customer)
