import mysql.connector
import os
from dotenv import load_dotenv
from flask import Flask
from models import db

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

if __name__ == "__main__":
    try:
        create_database()
        print("Database created successfully!")
        create_tables()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}") 