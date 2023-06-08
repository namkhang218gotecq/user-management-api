from pyrsistent import field
from boilerplate_api.query import customer

from fii_cqrs import resource as cr
from fii_cqrs.helper import nullable
from fii_cqrs.identifier import UUID_TYPE
from sanic_cqrs import PostgresCqrsResource

from boilerplate_api.model import  CardModel, UserModel, CustomerModel, TransactionrecordModel,SystemRoleModel




    
#----------------------------------------------------------------
@cr.register("user")
class UserResource(PostgresCqrsResource):
    __backend__ = UserModel

    _id = field(type=UUID_TYPE)
    username = field(type=str)
    password = field(type=str)
    status = field(type=str)
    
#----------------------------------------------------------------
@cr.register("system-role")
class SystemRoleResource(PostgresCqrsResource):
    __backend__ = SystemRoleModel
    
    _id = field(type=UUID_TYPE)
    name = field(type=str)
    key = field(type=str)
    description = field(type=str)
    active = field(type=bool)
    company_kind = field(type=str)








#----------------------------------------------------------------
@cr.register("card")
class CardResource(PostgresCqrsResource):
    __backend__ = CardModel

    _id = field(type=UUID_TYPE)
    password = field(type=nullable(str))
    balance = field(type=nullable(float))
    customer_id = field(type=UUID_TYPE)
#----------------------------------------------------------------
@cr.register("customer")
class CustomerResource(PostgresCqrsResource):
    __backend__ = CustomerModel

    _id = field(type=UUID_TYPE)
    identity_number = field(type=str)
    first_name = field(type=str)
    last_name = field(type=str)
    phone = field(type=str)
    address__city = field(type=str)

#----------------------------------------------------------------
@cr.register("transactionrecord")
class TransactionrecordResource(PostgresCqrsResource):
    __backend__ = TransactionrecordModel

    _id = field(type=UUID_TYPE)
    card_id = field(type=UUID_TYPE)
    transaction_type_id = field(type=UUID_TYPE)
    amount = field(type=float)
    message = field(type=str)

# ----------------------------------------------------------------


    