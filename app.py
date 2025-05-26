from flask import Flask, jsonify
from models import db
from schemas import ma
from routes import register_routes
import os

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)

    @app.route('/')
    def index():
        return """
            <h1>Welcome to the Flask API!</h1>
            <p>Available endpoints:</p>
            <ul>
                <li><a href="/product">/product</a></li>
                <li><a href="/customer">/customer</a></li>
                <li><a href="/functionality">/functionality</a></li>
                <li><a href="/order">/order</a></li>
            </ul>
            """

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
