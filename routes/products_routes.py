from flask import Blueprint, request, jsonify
from services.products_services import get_all_products

products_bp = Blueprint('product_bp', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products_route():
    products = get_all_products()

    return jsonify(products), 200