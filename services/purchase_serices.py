from flask_jwt_extended import get_jwt_identity
from database.models import db, Purchase, Product, purchase_products
from datetime import datetime

def create_purchase(jwt_identity, products_data):

    if not products_data:
        return {"message": "No products in body request."}, 400
    
    purchase_total_amount = 0
    purchase = Purchase(
        user_id=jwt_identity,
        total_amount=purchase_total_amount,
        created_at=datetime.now()
    )
    db.session.add(purchase)
    db.session.flush()

    for p in products_data:
        product = Product.query.filter_by(id=p['id']).first()  # Find the product
        if not product:
            return {"message": f"Product {p['id']} not found."}, 404
        if product.stock < p['quantity']:  # Check if stock is enough
            return {"message": f"Product {product.id} out of stock."}, 400
        
        product.stock -= p['quantity']
        purchase_total_amount += product.price * p['quantity']

        db.session.execute(
            purchase_products.insert().values(
                purchase_id=purchase.id,
                product_id=product.id,
                quantity=p['quantity'],
                price=product.price
            )
        )

    purchase.total_amount = purchase_total_amount
    db.session.commit()

    return {"message": "Purchase created successfully.", "id": purchase.id}, 201


def get_purchases(jwt_identity):
    purchases = Purchase.query.filter_by(user_id=jwt_identity).all()

    result = []
    for purchase in purchases:
        products_list = []
        for product in purchase.products:
            purchase_product = db.session.query(purchase_products).filter_by(
                    purchase_id=purchase.id,
                    product_id=product.id
                ).first()
            
            if purchase_product:
                products_list.append({
                    "id": product.id,
                    "name": product.name,
                    "quantity": purchase_product.quantity,
                    "price": purchase_product.price
                })

        result.append({
            "id": purchase.id,
            "total_amount": purchase.total_amount,
            "created_at": purchase.created_at,
            "products": products_list
        })
        
    return result