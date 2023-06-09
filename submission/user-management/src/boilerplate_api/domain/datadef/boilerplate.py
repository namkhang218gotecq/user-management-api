from pyrsistent import field
from boilerplate_api.query import customer
from sanic_validator.pyrsistent.factory import to_uuid

from fii_cqrs.command import CommandData
from fii_cqrs.event import EventData
from fii_cqrs.helper import nullable
from fii_cqrs.identifier import UUID_TYPE


import re


    
#----------------------------------------------------------------
class CreateUserData(CommandData):
    def validate_username(email):
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return email
        else:
            raise ValueError("Vui lòng nhập định dạng email hợp lệ!")

    def validate_password(password):
        if len(password) >= 8:
            return password
        else:
            raise ValueError("Mật khẩu phải chứa ít nhất 8 chữ cái")

    username = field(
        type=str,
        mandatory=True,
        factory=validate_username
    )
    password = field(
        type=str,
        mandatory=True,
        factory=validate_password
    )
    status = field(type=str, mandatory=True)

class CreateUserEventData(EventData):
    _id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)

    username = field(type=str, mandatory=True)
    password = field(type=str, mandatory=True)
    status = field(type=str, mandatory=True)

class UpdateUserData(CommandData):
    username = field(type=str, mandatory=True)
    password = field(type=str, mandatory=True)
    status = field(type=str, mandatory=True)
    
class UpdateUserEventData(EventData):
    username = field(type=str, mandatory=True)
    password = field(type=str, mandatory=True)
    status = field(type=str, mandatory=True)  
    
#----------------------------------------------------------------

class CreateSystemRoleData(CommandData):
    name = field(type=str, mandatory=True)
    key = field(type=str, mandatory=True)
    description = field(type=str, mandatory=True)
    active = field(type=bool, mandatory=True)
    company_kind = field(type=str, mandatory=True)

class CreateSystemRoleEventData(CommandData):
    _id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    
    name = field(type=str, mandatory=True)
    key = field(type=str, mandatory=True)
    description = field(type=str, mandatory=True)
    active = field(type=bool, mandatory=True)
    company_kind = field(type=str, mandatory=True)
    
#Create company
class CreateCompanyData(CommandData):
    
    status = field(type=str, mandatory=True)  
    kind = field(type=str, mandatory=True)  
    company_name = field(type=str, mandatory=True)
    telecom__email = field(type=str, mandatory=True)
    telecom__phone = field(type=str, mandatory=True)
    description = field(type=str, mandatory=True)
    address__postal = field(type=str, mandatory=True)
    address__state = field(type=str, mandatory=True)
    address__country = field(type=str, mandatory=True)
    tax_id = field(type=str, mandatory=True)
    category_name = field(type=str, mandatory=True)
    company_code = field(type=str, mandatory=True)
    npi = field(type=str, mandatory=True)
    
class CreateCompanyEventData(CommandData):
    _id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    
    status = field(type=str, mandatory=True)  
    kind = field(type=str, mandatory=True)  
    company_name = field(type=str, mandatory=True)
    telecom__email = field(type=str, mandatory=True)
    telecom__phone = field(type=str, mandatory=True)
    description = field(type=str, mandatory=True)
    address__postal = field(type=str, mandatory=True)
    address__state = field(type=str, mandatory=True)
    address__country = field(type=str, mandatory=True)
    tax_id = field(type=str, mandatory=True)
    category_name = field(type=str, mandatory=True)
    company_code = field(type=str, mandatory=True)
    npi = field(type=str, mandatory=True)
    
#Update company

class UpdateCompanyData(CommandData):
    status = field(type=nullable(str))  
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
    
class UpdateCompanyEventData(CommandData):
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#----------------------------------------------------------------
class CreateCardData(CommandData):
    password = field(type=str, mandatory=True)
    balance = field(type=float, mandatory=True)
    customer_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)

class CreateCardEventData(EventData):
    _id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)

    password = field(type=str, mandatory=True)
    balance = field(type=float, mandatory=True)
    customer_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)

#----------------------------------------------------------------
class CreateCustomerData(CommandData):
    identity_number = field(type=str, mandatory=True)
    first_name = field(type=str, mandatory=True)
    last_name = field(type=str, mandatory=True)
    phone = field(type=str, mandatory=True)
    address__city = field(type=str, mandatory=True)
    
    
class CreateCustomerEventData(EventData):
    _id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)

    identity_number = field(type=str, mandatory=True)
    first_name = field(type=str, mandatory=True)
    last_name = field(type=str, mandatory=True)
    phone = field(type=str, mandatory=True)
    address__city = field(type=str, mandatory=True)

class UpdateCustomerData(CommandData):
    first_name = field(type=str, mandatory=True)
    last_name = field(type=str, mandatory=True)
    
class UpdateCustomerEventData(EventData):
    first_name = field(type=str, mandatory=True)
    last_name = field(type=str, mandatory=True)


#----------------------------------------------------------------
class CreateTransactionrecordData(CommandData):
    card_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    transaction_type_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    amount = field(type=float, mandatory=True)
    message = field(type=str, mandatory=True)
  
    
    
class CreateTransactionrecordEventData(EventData):
    _id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    
    card_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    transaction_type_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    amount = field(type=float, mandatory=True)
    message = field(type=str, mandatory=True)
    
#----------------------------------------------------------------

# class WithdrawMoneyData(CommandData):
#     amount = field(type=float, mandatory=True)
    # factory validate (so am)

class WithdrawMoneyData(CommandData):
    def validate_amount(x):
        if x > 0:
            return x
        else:
            raise ValueError("Vui lòng nhập số hợp lệ!")

    amount = field(
        type=float,
        mandatory=True,
        factory=validate_amount
    )


class DepositMoneyData(CommandData):
    amount = field(type=float, mandatory=True)
    
class TransferMoneyData(CommandData):
    amount = field(type=float, mandatory=True)
    destination_card_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)

class CardUpdateEventData(EventData):
    balance = field(type=float)


class TransferMoneyEventData(EventData):
    source_card_id = field(type=UUID_TYPE,  mandatory=True)
    destination_card_id = field(type=UUID_TYPE, mandatory=True)
    amount = field(type=float, mandatory=True)