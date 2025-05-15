from flask_marshmallow import Marshmallow

ma = Marshmallow()

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

class FunctionalitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'product_id', 'name')

class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email')

class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'customer_id', 'amount', 'product_id')
