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
#db.create_all()
# Product Class/Model






# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
functionality_schema = FunctionalitySchema()
functionalities_schema = FunctionalitySchema(many=True)
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many = True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many = True)



# Run Server
if __name__ == '__main__':

  #Order.__table__.drop(engine)
  with app.app_context():
      db.create_all()
  app.run(host='0.0.0.0', debug=True)

