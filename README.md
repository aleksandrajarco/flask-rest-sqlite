a
# Flask REST SQLite

A simple RESTful API built with Flask and SQLite, demonstrating basic CRUD operations with SQLAlchemy and Marshmallow.

## Features

- REST API for managing Customers, Products, and Orders
- SQLite database with SQLAlchemy ORM
- Data validation and serialization with Marshmallow
- Modular project structure with Blueprints for routes and separate models

## Requirements

- Python 3.8+
- Flask 2.3.3
- Flask-SQLAlchemy 3.1.1
- Flask-Marshmallow 0.15.0
- marshmallow-sqlalchemy 0.29.0

You can install dependencies via:

```bash
pip install -r requirements.txt
```

## Setup & Run

1. Clone the repository:

```bash
git clone https://github.com/aleksandrajarco/flask-rest-sqlite.git
cd flask-rest-sqlite
```

2. Create a virtual environment and activate it (recommended):

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`

## API Endpoints

- `/customers` - Manage customers (GET, POST)
- `/customers/<id>` - Get, update, or delete a customer by ID
- `/products` - Manage products (GET, POST)
- `/products/<id>` - Get, update, or delete a product by ID
- `/orders` - Manage orders (GET, POST)
- `/orders/<id>` - Get, update, or delete an order by ID

Visit the root endpoint `/` to see a list of available endpoints.

## Docker

1. Build the Docker image:
```bash
docker build -t flaskapp .
```

2. Run the container:
```bash
docker run -d -p 5000:5000 flaskapp
```

3. Access the API at http://127.0.0.1:5000/


## Project Structure

```
flask-rest-sqlite/
├── app.py                  # Application factory and configuration
├── run.py                  # Entry point to launch the Flask app
├── models.py               # SQLAlchemy models for database tables
├── schemas.py              # Marshmallow schemas for validation and serialization
├── requirements.txt        # List of required Python packages
├── README.md               # Project documentation
├── db.sqlite               # SQLite database file (generated at runtime)

├── routes/                 # Modularized route definitions using Blueprints
│   ├── __init__.py         # Registers all route modules with the app
│   ├── customer.py         # Endpoints for Customer CRUD operations
│   ├── product.py          # Endpoints for Product CRUD operations
│   └── order.py            # Endpoints for Order CRUD operations
│   └── functionality.py    # Endpoints for Functionality CRUD operations
```

## License

MIT License

---



