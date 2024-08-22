from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required, role_required

def save():
    #POST request. /customers POST contain JSON
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer_save = customerService.save(customer_data)
    if customer_save is not None:
        return customer_schema.jsonify(customer_save), 201
    else: 
        return jsonify({"message":"Fallback method error activated", "body":customer_data}), 400


def update(id):
    
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer_update = customerService.update(customer_data, id)
    if customer_update is not None:
        return customer_schema.jsonify(customer_update), 200
    
# @cache.cached(timeout=60)   
@token_required
@role_required('admin') 
def find_all():
    customers = customerService.find_all()
    return customers_schema.jsonify(customers), 200


def find_customers_gmail():
    customers = customerService.find_customers_gmail()
    return customers_schema.jsonify(customers), 200

def find_all_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return customers_schema.jsonify(customerService.find_all_pagination(page=page, per_page=per_page)), 200

def find_one(id):
    customer = customerService.find_one(id)
    return customer_schema.jsonify(customer), 200

def delete(id):
    message=customerService.delete(id)
    return jsonify(message), 200
