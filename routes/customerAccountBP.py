from flask import Blueprint
from controllers.customerAccountController import update, find_all, login, find_one, save, delete

customer_account_blueprint= Blueprint('customer_account_bp', __name__)
customer_account_blueprint.route('/', methods=['POST'])(save) # Create
customer_account_blueprint.route('/<int:id>', methods=['GET'])(find_one) # Read
customer_account_blueprint.route('/', methods=['GET'])(find_all)
customer_account_blueprint.route('/login', methods=['POST'])(login)
customer_account_blueprint.route('/<int:id>', methods=['PUT'])(update)
customer_account_blueprint.route('/<int:id>', methods=['DELETE'])(delete)
