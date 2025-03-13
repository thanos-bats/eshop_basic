from database.models import db, Product, purchase_products

def get_all_products():
    products = Product.query.all()
    products_list = [{"id": product.id, "name": product.name, "price": product.price, "stock": product.stock, "created_at": product.created_at} for product in products]
    print(f"PRODUCT LIST:\n{products_list}")
    return products_list

def get_public_dashboard():
    products = Product.query.all()
    
    # Calculate statistics
    total_products = len(products)
    available_products = sum(1 for p in products if p.stock > 0)
    out_of_stock_products = sum(1 for p in products if p.stock == 0)
    
        
    # Get most purchased products
    most_purchased = (
            db.session.query(
                Product,
                db.func.sum(purchase_products.c.quantity).label('aggregate_quantity')
            )
            .join(purchase_products)
            .group_by(Product.id)
            .order_by(db.text('aggregate_quantity DESC'))
            .limit(2)
            .all()
        )
        
    most_purchased_products = [{
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "total_quantity_sold": int(quantity)
    } for product, quantity in most_purchased]
    
    return {
        "total_products": total_products,
        "available_products": available_products,
        "out_of_stock_products": out_of_stock_products,
        "most_purchased_products": most_purchased_products
    } 