from flask import Blueprint, request, jsonify
from services.products_services import get_all_products, get_public_dashboard

products_bp = Blueprint('product_bp', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products_route():
    products = get_all_products()

    return jsonify(products), 200

@products_bp.route('/public/dashboard', methods=['GET'])
def get_public_dashboard_route():
    stats = get_public_dashboard()

    return jsonify(stats), 200
