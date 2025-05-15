from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.String(100), db.ForeignKey('product.id'))
    name = db.Column(db.String(200))

    def __init__(self, name, product_id):
        self.product_id = product_id
        self.name = name


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(Customer.id))
    amount = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))

    def __init__(self, customer_id, amount, product_id):
        self.customer_id = customer_id
        self.amount = amount
        self.product_id = product_id
