from pyrsistent import field

from fii_cqrs import resource as cr
from fii_cqrs.helper import nullable
from fii_cqrs.identifier import UUID_TYPE
from sanic_cqrs import PostgresCqrsResource
from datetime import date, datetime

from boilerplate_api.model import   UserModel ,SystemRoleModel, CompanyModel, ProfileModel,CompanyRoleModel




    
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
    gender = field(type=nullable(str))
    birth_date = field(type=nullable(datetime))
    name__suffix = field(type=nullable(str))
    name__prefix = field(type=nullable(str))
    name__middle = field(type=nullable(str))
    avatar = field(type=nullable(UUID_TYPE))

@cr.register("company-profile")
class CompanyRoleResource(PostgresCqrsResource):
    __backend__ = CompanyRoleModel

    _id = field(type=UUID_TYPE)

    profile_id = field(type=UUID_TYPE)
    company_id = field(type=UUID_TYPE)
    role_id = field(type=UUID_TYPE)





















































