from database.models import db, Product

def get_all_products():
    products = Product.query.all()
    products_list = [{"id": product.id, "name": product.name, "price": product.price, "stock": product.stock, "created_at": product.created_at} for product in products]
    print(f"PRODUCT LIST:\n{products_list}")
    return products_list