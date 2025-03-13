import mysql.connector
import os
from dotenv import load_dotenv
from flask import Flask
import sys
try:
    from models import db, Product
except ImportError:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from eshop_api.database.models import db, Product

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME", "eshop")

def create_database():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

    cursor.close()
    conn.close()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app

def create_tables():
    app = create_app()
    with app.app_context():
        db.create_all()
        print(f"Tables created successfully!")

products = [
    {"name": "Laptop Lenovo", "price": 1000.99, "stock": 10},
    {"name": "Apple MacBook Air M3", "price": 1099.89, "stock": 5},
    {"name": "Dell Inspiron 15", "price": 899.99, "stock": 7},
    {"name": "Logitech Mouse MX", "price": 89.99, "stock": 20},
    {"name": "Razer Basilisk Mouse", "price": 46.88, "stock": 15},
    {"name": "Logitech Lift Vertical", "price": 49.99, "stock": 30},
    {"name": "Samsung Galaxy S21", "price": 999.99, "stock": 10},
    {"name": "iPhone 16", "price": 1199.99, "stock": 2},
    {"name": "Gaming Chair", "price": 299.99, "stock": 5}
]

def populate_products():
    app = create_app()
    with app.app_context():
        for product in products:
            if not check_if_products_exist(product):
                new_product = Product(name=product["name"], price=product["price"], stock=product["stock"])
                db.session.add(new_product)
        
        db.session.commit()
        print("Products added successfully!")

def check_if_products_exist(product):
    return Product.query.filter_by(name=product['name']).first()

if __name__ == "__main__":
    try:
        create_database()
        print("Database created successfully!")
        create_tables()
        
        populate_products()
    except Exception as e:
        print(f"An error occurred: {str(e)}") 