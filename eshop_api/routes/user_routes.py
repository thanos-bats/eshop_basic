from flask import Blueprint, request, jsonify
from services.user_services import register_user, login_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register_route():
    try:
        data = request.json
        response, status_code = register_user(data)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@user_bp.route('/login', methods=['POST'])
def login_route():
    try:
        data = request.json
        response, status_code = login_user(data)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
