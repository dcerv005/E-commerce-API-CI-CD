from sqlalchemy.orm import Mapped, mapped_column
from database import Base, db

class CustomerManagementRole(Base):
    __tablename__ = "Customer_Management_Roles"
    id : Mapped[int] = mapped_column(primary_key=True)
    customer_management_id : Mapped[int] = mapped_column(db.ForeignKey('Customer_Account.id'))
    role_id : Mapped[int] = mapped_column(db.ForeignKey('Roles.id'))