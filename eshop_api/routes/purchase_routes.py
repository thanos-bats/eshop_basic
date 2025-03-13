from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.purchase_serices import create_purchase, get_purchases, get_admin_dashboard

purchase_bp = Blueprint('purchase_bp', __name__)

@purchase_bp.route('/purchase', methods=['POST'])
@jwt_required()
def create_purchase_route():
    try:
        data = request.json
        products_data = data.get('products', [])

        jwt_identity = get_jwt_identity()
        response, status_code = create_purchase(jwt_identity, products_data)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
@purchase_bp.route('/purchases', methods=['GET'])
@jwt_required()
def get_purchases_route():
    try:
        jwt_identity = get_jwt_identity()
        user_purchases = get_purchases(jwt_identity)
        print(f"user purchases: {user_purchases}")
        return jsonify({"user_id:": jwt_identity, "purchases": user_purchases}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
@purchase_bp.route('/admin/dashboard', methods=['GET'])
@jwt_required()
def admin_dashboard_route():
    try:
        jwt_identity = get_jwt_identity()
        print(f"user is {jwt_identity}")
        data, status_code = get_admin_dashboard(jwt_identity)
        return jsonify(data), status_code
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
