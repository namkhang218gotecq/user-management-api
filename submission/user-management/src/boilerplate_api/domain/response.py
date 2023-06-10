from pyrsistent import PClass

from fii_cqrs.command import field
from fii_cqrs.response import CqrsResponse

from .domain import BoilerplateDomain

_entity = BoilerplateDomain.entity


def to_dict(data):
    if isinstance(data, PClass):
        return data.serialize()

    return data
#----------------------------------------------------------------

@_entity("user-response")
class UserResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True)
        
#----------------------------------------------------------------

@_entity("system-role-response")
class SystemRoleResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True)

#company
@_entity("company-response")
class CompanyResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True) 

#profile
@_entity("profile-response")
class ProfileResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True) 

    


    
    


    
    


    

#----------------------------------------------------------------

@_entity("card-response")
class CardResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True)
#----------------------------------------------------------------
@_entity("customer-response")
class CustomerResponse(CqrsResponse):
    data = field(type=dict, factory=to_dict, mandatory=True)
    

#----------------------------------------------------------------

@_entity("general-response")
class GeneralResponse(CqrsResponse):
    data = field(type=dict, mandatory=True)

