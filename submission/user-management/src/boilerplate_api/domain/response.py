from pyrsistent import PClass

from fii_cqrs.command import field
from fii_cqrs.response import CqrsResponse

from .domain import BoilerplateDomain

_entity = BoilerplateDomain.entity


def to_dict(data):
    if isinstance(data, PClass):
        return data.serialize()

    return data


@_entity("boilerplate-response")
class BoilerplateResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True)

#----------------------------------------------------------------

@_entity("card-response")
class CardResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True)
    
#----------------------------------------------------------------

@_entity("bank-response")
class BankResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True)
    
#----------------------------------------------------------------

@_entity("customer-response")
class BankResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True)
    
#----------------------------------------------------------------

@_entity("transactiontype-response")
class TransactiontypeResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True)
    
#----------------------------------------------------------------

@_entity("transactionrecord-response")
class TransactionrecordResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True)
    
@_entity("general-response")
class GeneralResponse(CqrsResponse):
    data = field(type=dict, mandatory=True)
