from flask import Blueprint, request, jsonify
from models import db, Functionality
from schemas import FunctionalitySchema

functionality_bp = Blueprint('functionality', __name__)

functionality_schema = FunctionalitySchema()
functionalities_schema = FunctionalitySchema(many=True)

@functionality_bp.route('/functionality', methods=['POST'])
def add_functionality():
    name = request.json['name']
    product_id = request.json['product_id']

    new_functionality = Functionality(name, product_id)
    db.session.add(new_functionality)
    db.session.commit()

    return functionality_schema.jsonify(new_functionality)

@functionality_bp.route('/functionality', methods=['GET'])
def get_functionalities():
    all_functionalities = Functionality.query.all()
    result = functionalities_schema.dump(all_functionalities)
    return jsonify(result)

@functionality_bp.route('/functionality/<int:id>', methods=['GET'])
def get_functionality(id):
    functionality = Functionality.query.get_or_404(id)
    return functionality_schema.jsonify(functionality)

@functionality_bp.route('/functionality/<int:id>', methods=['PUT'])
def update_functionality(id):
    functionality = Functionality.query.get_or_404(id)
    functionality.name = request.json['name']
    functionality.product_id = request.json['product_id']

    db.session.commit()
    return functionality_schema.jsonify(functionality)

@functionality_bp.route('/functionality/<int:id>', methods=['DELETE'])
def delete_functionality(id):
    functionality = Functionality.query.get_or_404(id)
    db.session.delete(functionality)
    db.session.commit()

    return functionality_schema.jsonify(functionality)
