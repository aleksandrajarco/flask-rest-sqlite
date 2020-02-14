from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Table, Column, Integer, ForeignKey, create_engine
import os
from sqlalchemy.sql.expression import func



# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
url = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
engine = create_engine(url, echo=False)
app.config['SQLALCHEMY_DATABASE_URI'] = url
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

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
      self.name = name
      self.email = email

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey(Customer.id))
    amount = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))

    def __init__(self, customer_id, amount, product_id):
      self.customer_id = customer_id
      self.amount = amount
      self.product_id = product_id

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

# Functionality Schema
class FunctionalitySchema(ma.Schema):
  class Meta:
    fields = ('id', 'product_id', 'name')

#Customer Schema
class CustomerSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'email')

#Order Schema
class OrderSchema(ma.Schema):
  class Meta:
    fields = ('id', 'customer_id', 'amount', 'product_id')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
functionality_schema = FunctionalitySchema()
functionalities_schema = FunctionalitySchema(many=True)
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many = True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many = True)

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


# Add new customer
@app.route('/customer', methods = ['POST'])
def add_customer():

  name = request.json['name']
  email = request.json['email']
  customer = Customer(name, email)

  db.session.add(customer)
  db.session.commit()
  return customer_schema.jsonify(customer)

# Update customer
@app.route('/customer/<id>', methods= ['PUT'])
def update_customer(id):
  customer = Customer.query.get(id)
  name = request.json['name']
  email = request.json['email']
  customer.name = name
  customer.email = email

  db.session.commit()

  return customer_schema.jsonify(customer)

# Get customer by id
@app.route('/customer/<id>', methods = ['GET'])
def get_customer(id):
  customer = Customer.query.get(id)
  result = customer_schema.jsonify(customer)

  db.session.commit()
  return result

# get all customers
@app.route('/customer', methods=['GET'])
def get_customers():
  customers=  Customer.query.all()
  result = functionalities_schema.dump(customers)
  return jsonify(result)


# delete customer
@app.route('/customer/<id>', methods = ['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()
    return customer_schema.jsonify(customer)



# Add new order
@app.route('/order', methods = ['POST'])
def add_order():
  customer_id = request.json['customer_id']
  amount = request.json['amount']
  product_id = request.json['product_id']
  order = Order(customer_id, amount, product_id)
  db.session.add(order)
  db.session.commit()
  return order_schema.jsonify(order)


#Update order
@app.route('/order/<id>', methods = ['POST'])
def upate_order(id):

    order = Order.query.get(id)
    order.customer_id = request.json['customer_id']
    order.amount = request.json['amount']
    order.product_id = request.json['product_id']
    db.session.commit()
    return order_schema.jsonify(order)


#get Single order
@app.route('/order/<id>', methods = ['GET'])
def get_single_order(id):
    order = Order.query.get(id)
    return order_schema.jsonify(order)

# get all orders
@app.route('/order', methods=['GET'])
def get_orders():
  orders=  Order.query.all()
  result = orders_schema.dump(orders)
  return jsonify(result)

# Run Server
if __name__ == '__main__':

  #Order.__table__.drop(engine)
  db.create_all()
  app.run(host='0.0.0.0', debug=True)

