from sqlalchemy import select
from sqlalchemy.orm import Session
from models.customer import Customer
from models.customerAccount import CustomerAccount
from database import db
from utils.util import encode_token
from werkzeug.security import check_password_hash

def find_all():
    query= select(CustomerAccount).join(Customer).where(Customer.id==CustomerAccount.customer_id)
    customer_accounts = db.session.execute(query).scalars().all()
    return customer_accounts

def find_one(id):
    query = select(CustomerAccount).where(CustomerAccount.id == id)
    customerAccount = db.session.execute(query).scalars().one()
    return customerAccount

def save(customerAccount_data):
    
        new_customerAccount = CustomerAccount(username=customerAccount_data["username"], password = customerAccount_data["password"], customer_id=customerAccount_data["customer"]["id"])
        db.session.add(new_customerAccount)
        db.session.commit()
        db.session.refresh(new_customerAccount)
        return new_customerAccount

def login_customer(username, password):
    user = (db.session.execute(db.select(CustomerAccount).where(CustomerAccount.username == username)).scalar_one_or_none())
    role_names = [role.role_name for role in user.roles]
    if user:
        if check_password_hash(user.password, password):
            auth_token = encode_token (user.id, role_names)
            resp = {
                'status': 'success',
                'message': 'Successfully logged in',
                'auth_token': auth_token
            }
            return resp
        else:
            return None
    else: 
        return None
    
def delete(id):
    query = select(CustomerAccount).where(CustomerAccount.id == id)
    customerAccount = db.session.execute(query).scalars().one()
    db.session.delete(customerAccount)
    db.session.commit()

    return {'message': 'Customer Account removed successfully'}

def update(customerAccount_data, id):
    query = select(CustomerAccount).where(CustomerAccount.id == id)
    customerAccount = db.session.execute(query).scalars().one()
    try:
        
                
        customerAccount.username=customerAccount_data["username"]
        customerAccount.password = customerAccount_data["password"]
        customerAccount.customer_id=customerAccount_data["customer"]["id"]
        db.session.commit()
        
            
        return customerAccount
    except Exception as e:
        raise e
