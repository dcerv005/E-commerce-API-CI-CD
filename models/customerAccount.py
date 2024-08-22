from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class CustomerAccount(Base):
    __tablename__ = 'Customer_Account'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('Customers.id'))
    #One-to-one: CustomerAccount and Customer
    customer: Mapped["Customer"] = db.relationship(back_populates="customer_account", lazy='select') # Eager Loading lazy="select"; Lazy Loading lazy='lazy' 
    # Many-to-Many : Roles and CustomerAccount with no back_populates
    roles: Mapped[List["Role"]] = db.relationship(secondary = "Customer_Management_Roles")