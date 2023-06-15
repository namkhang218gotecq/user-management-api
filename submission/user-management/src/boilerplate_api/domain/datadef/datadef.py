from pyrsistent import field
from sanic_validator.pyrsistent.factory import to_uuid, str_to_datetime 

from fii_cqrs.command import CommandData
from fii_cqrs.event import EventData
from fii_cqrs.helper import nullable
from fii_cqrs.identifier import UUID_TYPE
from datetime import date, datetime

import re


    
#----------------------------------------------------------------
class CreateUserData(CommandData):
    def validate_username(email):
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return email
        else:
            raise ValueError("Vui lòng nhập định dạng email hợp lệ!")

    def validate_password(password):
        if len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'\d', password):
            return password
        else:
            raise ValueError("Mật khẩu phải chứa ít nhất 8 chữ cái và ít nhất một chữ cái hoa và một chữ số")
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

class CreateUserEventData(EventData):
    _id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)

    username = field(type=str, mandatory=True)
    password = field(type=str, mandatory=True)
    status = field(type=str, mandatory=True)

class UpdateUserData(CommandData):
    username = field(type=str, mandatory=True)
    password = field(type=str, mandatory=True)
class UpdateUserEventData(EventData):
    username = field(type=nullable(str))
    password = field(type=nullable(str))
    
    
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
    
    kind = field(nullable(str))  
    company_name = field(nullable(str))
    telecom__email = field(nullable(str))
    telecom__phone = field(nullable(str))
    description = field(nullable(str))
    address__postal = field(nullable(str))
    address__state = field(nullable(str))
    address__country = field(nullable(str))
    tax_id = field(nullable(str))
    category_name = field(nullable(str))
    company_code = field(nullable(str))
    npi = field(nullable(str))
    
class CreateCompanyEventData(CommandData):
    _id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    
    status = field(nullable(str))  
    kind = field(nullable(str))  
    company_name = field(nullable(str))
    telecom__email = field(nullable(str))
    telecom__phone = field(nullable(str))
    description = field(nullable(str))
    address__postal = field(nullable(str))
    address__state = field(nullable(str))
    address__country = field(nullable(str))
    tax_id = field(nullable(str))
    category_name = field(nullable(str))
    company_code = field(nullable(str))
    npi = field(nullable(str))
    
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
    status = field(type=nullable(str))  
    kind = field(type=nullable(str))  
    company_name = field(type=nullable(str))
    telecom__email = field(type=nullable(str))
    telecom__phone = field(type=nullable(str))
    description = field(type=nullable(str))
    address__postal = field(type=nullable(str))
    address__state = field(type=nullable(str))
    address__country = field(type=nullable(str))
    tax_id = field(type=nullable(str))
    category_name = field(type=nullable(str))
    company_code = field(type=nullable(str))
    npi = field(type=nullable(str))
    
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
    birth_date = field(type=datetime)
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
    birth_date = field(type=nullable(datetime))
    name__suffix = field(type=nullable(str))
    name__prefix = field(type=nullable(str))
    name__middle = field(type=nullable(str))
    avatar = field(type=nullable(UUID_TYPE), factory=to_uuid)
    
# Update profile

class UpdateProfileData(CommandData):
    
    _id = field(type=UUID_TYPE, factory=to_uuid)
    
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
    birth_date = field(type=nullable(datetime))
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
    birth_date = field(type=nullable(datetime))
    name__suffix = field(type=nullable(str))
    name__prefix = field(type=nullable(str))
    name__middle = field(type=nullable(str))
    avatar = field(type=nullable(UUID_TYPE), factory=to_uuid)  
    
    
class UpdateStatusProfileData(CommandData):
    pass
    
class UpdateStatusEventProfile(CommandData):
    status = field(type=(str))

class UpdateStatusAccountData(CommandData):
    pass

class UpdateStatusAccountEvent(CommandData):
    status = field(type=(str))

class UpdateStatusCompanyData(CommandData):
    pass

class UpdateStatusCompanyEvent(CommandData):
    status = field(type=(str))
    
# company-profile

class CompanyRoleData(CommandData):
    
    profile_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    company_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    role_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
class CompanyRoleEventData(CommandData):
    _id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    
    profile_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    company_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    role_id = field(type=UUID_TYPE, factory=to_uuid, mandatory=True)
    
    

    
    
    
    
    
    
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    