from flask import Blueprint
from controllers.customerController import delete, save, find_all, find_customers_gmail, find_all_pagination, update, find_one

customer_blueprint= Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['POST'])(save) #Create
customer_blueprint.route('/<int:id>', methods=['GET'])(find_one) #READ
customer_blueprint.route('/<int:id>', methods=['PUT'])(update) #Update
customer_blueprint.route('/<int:id>', methods=['DELETE'])(delete) #Delete
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/gmail', methods=['GET'])(find_customers_gmail)
customer_blueprint.route('/paginate', methods=['GET'])(find_all_pagination)



