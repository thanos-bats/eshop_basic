from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.purchase_serices import create_purchase

purchase_bp = Blueprint('purchase_bp', __name__)

@purchase_bp.route('/purchase', methods=['POST'])
@jwt_required()
def create_purchase_route():
    try:
        data = request.json
        products_data = data.get('products', [])

        jwt_idenity = get_jwt_identity()
        response, status_code = create_purchase(jwt_idenity, products_data)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
