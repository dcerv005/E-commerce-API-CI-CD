from flask import request, jsonify
from models.schemas.customerAccountSchema import customerAccounts_schema, customerAccount_schema
from services import customerAccountService
from marshmallow import ValidationError
from caching import cache

def find_all():
    customer_accounts = customerAccountService.find_all()
    return customerAccounts_schema.jsonify(customer_accounts)

def find_one(id):
    customerAccount = customerAccountService.find_one(id)
    return customerAccount_schema.jsonify(customerAccount), 200

def save():
    #POST request. /customers POST contain JSON
    try:
        customerAccount_data = customerAccount_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customerAccount_save = customerAccountService.save(customerAccount_data)
    if customerAccount_save is not None:
        return customerAccount_schema.jsonify(customerAccount_save), 201
    else: 
        return jsonify({"message":"Fallback method error activated", "body":customerAccount_data}), 400


def login():
    customer = request.json
    user = customerAccountService.login_customer(customer['username'], customer['password'])
    if user:
        return jsonify(user), 200
    
    else: 
        resp = {
            'status' : 'Error',
            'message' : 'User does not exist'
        }
        return jsonify(resp), 404
    
def delete(id):
    message=customerAccountService.delete(id)
    return jsonify(message), 200

def update(id):
    try:
        customerAccount_data = customerAccount_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customerAccount_update = customerAccountService.update(customerAccount_data, id)
    if customerAccount_update is not None:
        return customerAccount_schema.jsonify(customerAccount_update), 200