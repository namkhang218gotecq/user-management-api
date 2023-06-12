from pyrsistent import field
from boilerplate_api.query import customer

from fii_cqrs import resource as cr
from fii_cqrs.helper import nullable
from fii_cqrs.identifier import UUID_TYPE
from sanic_cqrs import PostgresCqrsResource
from datetime import date

from boilerplate_api.model import  CardModel, UserModel, CustomerModel, TransactionrecordModel,SystemRoleModel, CompanyModel, ProfileModel, StatusProfileModel




    
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

@cr.register("company")
class CompanyResource(PostgresCqrsResource):
    __backend__ = CompanyModel

    _id = field(type=UUID_TYPE)
    status = field(type=str)
    kind = field(type=str)
    company_name = field(type=str)
    telecom__email = field(type=str)
    telecom__phone = field(type=str)
    description = field(type=str)
    address__postal = field(type=str)
    address__state = field(type=str)
    address__country = field(type=str)
    tax_id = field(type=str)
    category_name = field(type=str)
    company_code = field(type=str)
    npi = field(type=str)


@cr.register("profile")
class ProfileResource(PostgresCqrsResource):
    __backend__ = ProfileModel

    _id = field(type=UUID_TYPE)
    
    account_id = field(type=UUID_TYPE)
    company_id = field(type=UUID_TYPE)
    status = field(type=str, mandatory=True)
    name__family = field(type=str, mandatory=True)
    name__given = field(type=str, mandatory=True)
    telecom__email = field(type=nullable(str))
    telecom__phone = field(type=nullable(str))
    address__postal = field(type=nullable(str))
    address__state = field(type=nullable(str))
    address__country = field(type=nullable(str))
    address__line = field(type=nullable(str))
    gender = field(type=str)
    birth_date = field(type=nullable(date))
    name__suffix = field(type=nullable(str))
    name__prefix = field(type=nullable(str))
    name__middle = field(type=nullable(str))
    avatar = field(type=nullable(UUID_TYPE))




























































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


    