from fii_cqrs.command import Command, field
from fii_cqrs.identifier import UUID_GENR

from boilerplate_api.domain.datadef import  CreateUserData, UpdateUserData,CreateSystemRoleData,CreateCompanyData, UpdateCompanyData,CreateProfileData, UpdateProfileData, CreateProfileEventData
from ..domain import BoilerplateDomain
from .helper import combine_profile_status
_entity = BoilerplateDomain.entity
_handler = BoilerplateDomain.command_handler



#  user
@_entity("create-user") 
class CreateUser(Command):
    data = field(type=CreateUserData)

    class Meta:
        resource = "user"
        tags = ["user"]
        description = "Create new user"

@_handler(CreateUser)
async def handle_create_user(aggproxy, cmd: CreateUser):
    
    event = await aggproxy.create_user(cmd.data)
    yield event
    yield aggproxy.create_response(
        "user-response", cmd, {"_id": event.data._id}
    )
# Update user
@_entity
class UpdateUser(Command):
    data = field(type=UpdateUserData, mandatory=True)
    
    class Meta:
        resource = "user/{id}"
        tags = ["user"]
        description = "Update user information"
        parameters = [
            {
                "name": "id",
                "in": "path",
                "description": "User ID: ",
                "required": True,
                "schema": {
                    "type": "string",
                },
            }
        ]


@_handler(UpdateUser)
async def handle_update_user(aggproxy, cmd: UpdateUserData):
    event = await aggproxy.update_user(cmd.data)
    yield event

#Create system role 
@_entity("create-system-role") 
class CreateSystemRole(Command):
    data = field(type=CreateSystemRoleData)

    class Meta:
        resource = "system-role"
        tags = ["system-role"]
        description = "Create new system role"

@_handler(CreateSystemRole)
async def handle_create_system_role(aggproxy, cmd: CreateUser):
    
    event = await aggproxy.create_system_role(cmd.data)
    yield event
    yield aggproxy.create_response(
        "system-role-response", cmd, {"_id": event.data._id}
    )


# Create company
@_entity("create-company") 
class CreateCompany(Command):
    data = field(type=CreateCompanyData)

    class Meta:
        resource = "company"
        tags = ["company"]
        description = "Create new company"

@_handler(CreateCompany)
async def handle_create_company(aggproxy, cmd: CreateCompany):
    
    event = await aggproxy.create_company(cmd.data)
    yield event
    yield aggproxy.create_response(
        "company-response", cmd, {"_id": event.data._id}
    )

# Update company
@_entity
class UpdateCompany(Command):
    data = field(type=UpdateCompanyData, mandatory=True)
    
    class Meta:
        resource = "company/{id}"
        tags = ["company"]
        description = "Update company information"
        parameters = [
            {
                "name": "id",
                "in": "path",
                "description": "Company ID: ",
                "required": True,
                "schema": {
                    "type": "string",
                },
            }
        ]


@_handler(UpdateCompany)
async def handle_update_company(aggproxy, cmd: UpdateCompanyData):
    event = await aggproxy.update_company(cmd.data)
    yield event

# Create profile

@_entity("create-profile") 
class CreateProfile(Command):
    data = field(type=CreateProfileData)

    class Meta:
        resource = "profile"
        tags = ["profile"]
        description = "Create new profile"

@_handler(CreateProfile)
async def handle_create_profile(aggproxy, cmd: CreateProfileData):
    company = await aggproxy.state.fetch(
        "company",cmd.data.company_id
        )
    account = await aggproxy.state.fetch(
        "user",cmd.data.account_id
    )
    event_data = CreateProfileEventData.extend_pclass(
            pclass=cmd.data, _id=UUID_GENR(), status = combine_profile_status(account.status, company.status)
        )
    event = await aggproxy.create_profile(event_data)
    yield event
    yield aggproxy.create_response(
        "profile-response", cmd, {"_id": event.data._id}
    )
    

# Update profile
@_entity
class UpdateProfile(Command):
    data = field(type=UpdateProfileData, mandatory=True)
    
    class Meta:
        resource = "profile/{id}"
        tags = ["profile"]
        description = "Update profile information"
        parameters = [
            {
                "name": "id",
                "in": "path",
                "description": "Profile ID: ",
                "required": True,
                "schema": {
                    "type": "string",
                },
            }
        ]


@_handler(UpdateProfile)
async def handle_update_profile(aggproxy, cmd: UpdateProfileData):
    event = await aggproxy.update_profile(cmd.data)
    yield event





















