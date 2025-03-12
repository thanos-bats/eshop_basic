from flask import Blueprint, request, jsonify
from services.user_services import register_user, login_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register_route():
    data = request.json
    response = register_user(data)
    return jsonify(response)

@user_bp.route('/login', methods=['POST'])
def login_route():
    data = request.json
    response = login_user(data)
    return jsonify(response)
