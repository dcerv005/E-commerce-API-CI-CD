from models.product import Product
from database import db
from sqlalchemy.orm import Session
from sqlalchemy import select


def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data["name"], price = product_data["price"])
            session.add(new_product)
            session.commit()
        session.refresh(new_product)
        return new_product
    
def update_product(product_data, id):
    query = select(Product).where(Product.id == id)
    product = db.session.execute(query).scalars().one()
    try:
        if product_data['name'] == 'Failure':
            raise Exception("Failure condition triggered")
        # with Session(db.engine) as session:
        #     with session.begin():
                
        product.name=product_data['name']
        product.price=product_data['price']
        # breakpoint()
        db.session.commit()
        
            
        return product
    except Exception as e:
        raise e
    
def delete(id):
    query = select(Product).where(Product.id == id)
    product = db.session.execute(query).scalars().one()
    db.session.delete(product)
    db.session.commit()

    return {'message': 'Product removed successfully'}

def find_one(id):
    query = select(Product).where(Product.id == id)
    product = db.session.execute(query).scalars().one()
    return product

def find_all():
    query = select(Product)
    products = db.session.execute(query).scalars().all()
    return products