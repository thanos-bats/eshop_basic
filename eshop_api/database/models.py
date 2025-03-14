from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    purchases = db.relationship('Purchase', backref='user', lazy=True)

    __table_args__ = (
        db.Index('idx_username_is_admin', 'username', 'is_admin'),
    )

purchase_products = db.Table(
    'purchase_products',
    db.Column('purchase_id', db.Integer, db.ForeignKey('purchases.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('quantity', db.Integer, nullable=False),
    db.Column('price', db.DECIMAL(10,2), nullable=False),
    db.Column('created_at', db.DateTime, default=datetime.now)
)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)
    price = db.Column(db.DECIMAL(10,2), nullable=False)
    stock = db.Column(db.Integer, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    __table_args__ = (
        db.Index('idx_name_stock', 'name', 'stock'),
    )

class Purchase(db.Model):
    __tablename__ = 'purchases'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    total_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    products = db.relationship('Product', secondary='purchase_products', backref=db.backref('purchases', lazy=True), lazy=True)

    __table_args__ = (
        db.Index('idx_user_created', 'user_id', 'created_at'),
    )