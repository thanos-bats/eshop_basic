from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from database.models import db
from routes.user_routes import user_bp
from routes.products_routes import products_bp
from routes.purchase_routes import purchase_bp
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(user_bp)
app.register_blueprint(products_bp)
app.register_blueprint(purchase_bp)

if __name__ == "__main__":
    app.run(debug=True, port=4567)