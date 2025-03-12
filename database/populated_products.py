import os
from dotenv import load_dotenv
from models import db, Product
from init_db import create_app

load_dotenv()

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
    populate_products()