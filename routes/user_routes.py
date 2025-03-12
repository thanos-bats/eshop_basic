from flask import Blueprint, request, jsonify
from services.user_services import register_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register_route():
    data = request.json
    response = register_user(data)
    return jsonify(response)


