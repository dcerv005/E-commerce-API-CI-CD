from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from circuitbreaker import circuit
from sqlalchemy import select

def fallback_function (customer):
    return None


@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_function)
def save(customer_data):
    try: 
        if customer_data['name'] == 'Failure':
            raise Exception("Failure condition triggered")
        with Session(db.engine) as session:
            with session.begin():
                new_customer = Customer(name=customer_data['name'], email =customer_data['email'], phone=customer_data['phone'])
                session.add(new_customer)
                # session.commit()
                try: 
                    # Do query / transaction here
                    #save a nesged transaction and establisj a savepoint
                    savepoint = session.begin_nested()
                    new_nested_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
                    session.add(new_nested_customer)
                except:
                    # Rollback the nested transaction to the savepoint
                    savepoint.rollback() #the rollback would go back to the savepoint and erase all the code done after that save point and then continue

            session.refresh(new_customer)
            return new_customer
    except Exception as e:
        raise e

def update(customer_data, id):
    query = select(Customer).where(Customer.id == id)
    customer = db.session.execute(query).scalars().one()
    try:
        if not id or customer_data['name'] == 'Failure':
            raise Exception("Failure condition triggered")
        
        customer.name=customer_data['name']
        customer.email=customer_data['email']
        customer.phone=customer_data['phone']

        db.session.commit()
        
        return customer
    except Exception as e:
        raise e
    
def find_all():
    query = select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers
def find_one(id):
    query = select(Customer).where(Customer.id == id)
    customer = db.session.execute(query).scalars().one()
    return customer
def find_customers_gmail():
    query = select(Customer).where(Customer.email.like("%gmail%"))
    customers = db.session.execute(query).scalars().all()
    return customers

def find_all_pagination(page=1, per_page=10):
    customers = db.paginate(select(Customer), page=page, per_page=per_page)
    return customers

def delete(id):
    query = select(Customer).where(Customer.id == id)
    customer = db.session.execute(query).scalars().one()
    db.session.delete(customer)
    db.session.commit()

    return {'message': 'Customer removed successfully'}
  