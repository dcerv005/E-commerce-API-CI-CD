from flask import jsonify, request
from models.schemas.orderSchema import order_schema, order_schema_customer
from marshmallow import ValidationError
from services import orderService

def save():
    try:

        #Validate and deserialize input
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    try:
        order_save = orderService.save(order_data)
        return order_schema.jsonify(order_save), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def find_by_id(id):
    order = orderService.find_by_id(id)
    return order_schema.jsonify(order), 200    