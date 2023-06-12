from pyrsistent import field
from sanic_validator.pyrsistent.factory import to_uuid

from fii_cqrs.command import CommandData
from fii_cqrs.event import EventData
from fii_cqrs.helper import nullable
from fii_cqrs.identifier import UUID_TYPE
from datetime import date

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
    
# Create profile 
class CreateProfileData(CommandData):
    account_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    company_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    name__family = field(type=str, mandatory=True)
    name__given = field(type=str, mandatory=True)
    telecom__email = field(type=nullable(str))
    telecom__phone = field(type=nullable(str))
    address__postal = field(type=nullable(str))
    address__state = field(type=nullable(str))
    address__country = field(type=nullable(str))
    address__line = field(type=nullable(str))
    gender = field(type=str)
    birth_date = field(type=date)
    name__suffix = field(type=nullable(str))
    name__prefix = field(type=nullable(str))
    name__middle = field(type=nullable(str))
    avatar = field(type=nullable(UUID_TYPE), factory=to_uuid)
    
    
class CreateProfileEventData(CommandData):
    _id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    
    account_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    company_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
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
    avatar = field(type=nullable(UUID_TYPE), factory=to_uuid)
    
# Update profile

class UpdateProfileData(CommandData):
    status = field(type=nullable(str))
    name__family = field(type=nullable(str))
    name__given = field(type=nullable(str))
    telecom__email = field(type=nullable(str))
    telecom__phone = field(type=nullable(str))
    address__postal = field(type=nullable(str))
    address__state = field(type=nullable(str))
    address__country = field(type=nullable(str))
    address__line = field(type=nullable(str))
    gender = field(type=nullable(str))
    birth_date = field(type=nullable(date))
    name__suffix = field(type=nullable(str))
    name__prefix = field(type=nullable(str))
    name__middle = field(type=nullable(str))
    avatar = field(type=nullable(UUID_TYPE), factory=to_uuid)
    
class UpdateProfileEventData(CommandData):
    status = field(type=nullable(str))
    name__family = field(type=nullable(str))
    name__given = field(type=nullable(str))
    telecom__email = field(type=nullable(str))
    telecom__phone = field(type=nullable(str))
    address__postal = field(type=nullable(str))
    address__state = field(type=nullable(str))
    address__country = field(type=nullable(str))
    address__line = field(type=nullable(str))
    gender = field(type=nullable(str))
    birth_date = field(type=nullable(date))
    name__suffix = field(type=nullable(str))
    name__prefix = field(type=nullable(str))
    name__middle = field(type=nullable(str))
    avatar = field(type=nullable(UUID_TYPE), factory=to_uuid)  
    
    
class UpdateStatusProfileData(CommandData):

    account_id = field(type=nullable(UUID_TYPE), factory=to_uuid)
    company_id = field(type=nullable(UUID_TYPE), factory=to_uuid)
    account_status = field(type=(str))
    company_status = field(type=(str))
    profile_status = field(type=nullable(str))
    
class UpdateStatusEventProfile(CommandData):
    profile_status = field(type=(str))
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    