from flask import Blueprint
from controllers.productController import find_all, save, delete, find_one, update

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/<int:id>', methods=['GET'])(find_one)
product_blueprint.route('/<int:id>', methods=['DELETE'])(delete)
product_blueprint.route('/<int:id>', methods=['PUT'])(update)
product_blueprint.route('/', methods=['GET'])(find_all)
