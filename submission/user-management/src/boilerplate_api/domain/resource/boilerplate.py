from pyrsistent import field
from boilerplate_api.query import customer

from fii_cqrs import resource as cr
from fii_cqrs.helper import nullable
from fii_cqrs.identifier import UUID_TYPE
from sanic_cqrs import PostgresCqrsResource

from boilerplate_api.model import BoilerplateModel, CardModel, BankModel, CustomerModel, TransactiontypeModel, TransactionrecordModel


@cr.register("boilerplate")
class BoilerplateResource(PostgresCqrsResource):
    __backend__ = BoilerplateModel

    _id = field(type=UUID_TYPE)
    name = field(type=nullable(str))
    description = field(type=nullable(str))

#----------------------------------------------------------------
@cr.register("card")
class CardResource(PostgresCqrsResource):
    __backend__ = CardModel

    _id = field(type=UUID_TYPE)
    password = field(type=nullable(str))
    balance = field(type=nullable(float))
    customer_id = field(type=UUID_TYPE)
    
#----------------------------------------------------------------
@cr.register("bank")
class CardResource(PostgresCqrsResource):
    __backend__ = BankModel

    _id = field(type=UUID_TYPE)
    bank__name = field(type=str)
    address__line = field(type=str)
    address__city = field(type=str)
    address__state = field(type=str)
    address__country = field(type=str)
    postal__code = field(type=str)
    phone = field(type=str)
#----------------------------------------------------------------
@cr.register("customer")
class CustomerResource(PostgresCqrsResource):
    __backend__ = CustomerModel

    _id = field(type=UUID_TYPE)
    identity_number = field(type=str)
    fist_name = field(type=str)
    last_name = field(type=str)
    phone = field(type=str)
    address__city = field(type=str)

#----------------------------------------------------------------
@cr.register("transactiontype")
class TransactiontypeResource(PostgresCqrsResource):
    __backend__ = TransactiontypeModel

    _id = field(type=UUID_TYPE)
    transaction_type = field(type=str)
    description = field(type=str)

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


    