from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from database.models import db
from routes.user_routes import user_bp
from routes.products_routes import products_bp
from routes.purchase_routes import purchase_bp

# Load environment variables
load_dotenv()

# Database connection settings
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASS = os.getenv('DB_PASS', 'password')
DB_NAME = 'eshop'

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Configure JWT
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    
    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)
    
    # Register blueprints without prefixes
    app.register_blueprint(user_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(purchase_bp)
    
    # Define a simple route
    @app.route('/')
    def index():
        return "Welcome to the e-shop!"
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=3000, debug=True) 