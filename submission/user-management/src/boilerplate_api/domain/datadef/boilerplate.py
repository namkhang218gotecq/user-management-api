from pyrsistent import field
from boilerplate_api.query import customer
from sanic_validator.pyrsistent.factory import to_uuid

from fii_cqrs.command import CommandData
from fii_cqrs.event import EventData
from fii_cqrs.identifier import UUID_TYPE




    
#----------------------------------------------------------------
class CreateUserData(CommandData):
    username = field(type=str, mandatory=True)
    password = field(type=str, mandatory=True)
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