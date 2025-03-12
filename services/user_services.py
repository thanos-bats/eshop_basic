from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from database.models import db, User

def register_user(data):
    try:
        username = data['username']
        password = data['password']

        if User.query.filter_by(username=username).first():
            return {"message": "User already exists!"}, 400
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created successfully!"}, 201
    except Exception as e:
        return {"message": str(e)}, 500
    
def login_user(data):
    try:
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return {"message": "Invalid credentials!"}, 401
        
        access_token = create_access_token(identity=username)
        return {"access_token": access_token}, 200
    except Exception as e:
        return {"message": str(e)}, 500