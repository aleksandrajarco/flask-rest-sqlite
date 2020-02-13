from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Table, Column, Integer, ForeignKey
import os
from sqlalchemy.sql.expression import func



# Init app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)
db.create_all()
# Product Class/Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement = True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)
  functionalities = db.relationship('Functionality', backref='product')

  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty


class Functionality(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement = True)
  product_id = db.Column(db.String(100), ForeignKey('product.id'))
  name = db.Column(db.String(200))

  def __init__(self, name, product_id):
    self.product_id = product_id
    self.name = name

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

# Functionality Schema
class FunctionalitySchema(ma.Schema):
  class Meta:
    fields = ('id', 'product_id', 'name')


# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
functionality_schema = FunctionalitySchema()
functionalities_schema = FunctionalitySchema(many=True)

# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  new_product = Product(name, description, price, qty)

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)


# Get All Products
@app.route('/product', methods = ['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

# Get Single Products
@app.route('/product/<id>', methods = ['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)


# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)
  product.name = request.json['name']
  product.description = request.json['description']
  product.price = request.json['price']
  product.qty = request.json['qty']

  db.session.commit()

  return product_schema.jsonify(product)

# Delete product
@app.route('/product/<id>', methods = ['DELETE'])
def delete_product(id):
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)

# Create a functionality
@app.route('/functionality', methods=['POST'])
def add_functionality():
  name = request.json['name']
  product_id = request.json['product_id']
  new_functionality = Functionality(name, product_id)

  db.session.add(new_functionality)
  db.session.commit()

  return product_schema.jsonify(new_functionality)


# Get All Functionalities
@app.route('/functionality', methods=['GET'])
def get_functionalities():
  all_functionalities= Functionality.query.all()
  result = functionalities_schema.dump(all_functionalities)
  return jsonify(result)


# Get Single Functionality
@app.route('/functionality/<id>', methods=['GET'])
def get_functionality(id):
  functionality = Functionality.query.get(id)
  return functionality_schema.jsonify(functionality)

# Update a Functionality
@app.route('/functionality/<id>', methods=['PUT'])
def update_functionality(id):
  functionality = Functionality.query.get(id)
  functionality.name = request.json['name']
  functionality.product_id = request.json['product_id']

  db.session.commit()

  return functionality_schema.jsonify(functionality)

# Delete functionality
@app.route('/functionality/<id>', methods = ['DELETE'])
def delete_functionality(id):
    functionality = Functionality.query.get(id)

    db.session.delete(functionality)
    db.session.commit()

    return functionality_schema.jsonify(functionality)

# Run Server
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  #db.drop_all()
  db.create_all()