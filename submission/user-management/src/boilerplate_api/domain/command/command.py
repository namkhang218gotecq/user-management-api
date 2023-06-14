from fii_cqrs.command import Command, field
from fii_cqrs.identifier import UUID_GENR

from boilerplate_api.domain.datadef import  CreateUserData, UpdateUserData,CreateSystemRoleData,CreateCompanyData, UpdateCompanyData,CreateProfileData, UpdateProfileData, CreateProfileEventData, UpdateStatusProfileData, UpdateStatusAccountData,CompanyRoleData, CreateUserEventData, UpdateUserEventData,UpdateStatusCompanyData,CreateCompanyEventData
from ..domain import BoilerplateDomain
from .helper import combine_profile_status
_entity = BoilerplateDomain.entity
_handler = BoilerplateDomain.command_handler
from boilerplate_api import __version__, config


#  user
@_entity("create-user") 
class CreateUser(Command):
    data = field(type=CreateUserData)

    class Meta:
        resource = "user"
        tags = ["user"]
        description = "Create new user"

@_handler(CreateUser)
async def handle_create_user(aggproxy, cmd: CreateUserData):
    
    event_data = CreateUserEventData.extend_pclass(
            pclass=cmd.data, _id=UUID_GENR(), status = "ACTIVE"
        )
    
    event = await aggproxy.create_user(event_data)
    yield event
    yield aggproxy.create_response(
        "user-response", cmd, {"_id": event.data._id}
    )
    yield aggproxy.log_activity(
        logroot={
            "identifier": cmd.aggroot.identifier,
            "resource": cmd.aggroot.resource,
            "namespace": config.BOILERPLATE_API_DOMAIN,
        },
        message=f"create user with email <b>{event_data.username}</b>",
        msglabel="create-user",
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
    
# Deactivate account
@_entity
class DeactivateAccount(Command):
    data = field(type=UpdateStatusAccountData, mandatory=True)
    
    class Meta:
        resource = "user/{id}"
        tags = ["user"]
        description = "Deactivate account"
        parameters = [
            {
                "name": "id",
                "in": "path",
                "description": "Account ID: ",
                "required": True,
                "schema": {
                    "type": "string",
                },
            }
        ]
        
@_handler(DeactivateAccount)
async def handle_deactivate_account(aggproxy, cmd: UpdateStatusAccountData):
    profile_list = await aggproxy.state.find(
        "profile",
        data_query = {
            "where": {
                "account_id": cmd.aggroot.identifier,
                
            }   
        }
    )
    for profile in profile_list:
        company = await aggproxy.state.fetch(
            "company", profile.company_id
        )
        event_status_user = await aggproxy.update_profile(UpdateProfileData(status = combine_profile_status("INACTIVE", company.status), _id = profile._id))
        yield event_status_user
    
    
    event = await aggproxy.deactivate_account(cmd.data)
    yield event

# Activate account
@_entity
class ActivateAccount(Command):
    data = field(type=UpdateStatusAccountData, mandatory=True)
    
    class Meta:
        resource = "user/{id}"
        tags = ["user"]
        description = "Activate account"
        parameters = [
            {
                "name": "id",
                "in": "path",
                "description": "Account ID: ",
                "required": True,
                "schema": {
                    "type": "string",
                },
            }
        ]
        
@_handler(ActivateAccount)
async def handle_activate_account(aggproxy, cmd: UpdateStatusAccountData):
    profile_list = await aggproxy.state.find(
        "profile",
        data_query = {
            "where": {
                "account_id": cmd.aggroot.identifier,
                
            }   
        }
    )
    for profile in profile_list:
        company = await aggproxy.state.fetch(
            "company", profile.company_id
        )
        event_status_user = await aggproxy.update_profile(UpdateProfileData(status = combine_profile_status("ACTIVE", company.status), _id = profile._id))
        yield event_status_user
    
    
    
    event = await aggproxy.activate_account(cmd.data)
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
    
    event_data = CreateCompanyEventData.extend_pclass(
            pclass=cmd.data, _id=UUID_GENR(), status = "ACTIVE"
        )
    event = await aggproxy.create_company(event_data)
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

# Deactivate company
@_entity
class DeactivateCompany(Command):
    data = field(type=UpdateStatusCompanyData, mandatory=True)
    
    class Meta:
        resource = "company/{id}"
        tags = ["company"]
        description = "Deactivate company"
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
        
@_handler(DeactivateCompany)
async def handle_deactivate_company(aggproxy, cmd: UpdateStatusCompanyData):
    profile_list = await aggproxy.state.find(
        "profile",
        data_query = {
            "where": {
                "company_id": cmd.aggroot.identifier,
                
            }   
        }
    )
    for profile in profile_list:
        account = await aggproxy.state.fetch(
        "user", profile.account_id
        )
        event_status_company = await aggproxy.update_profile(UpdateProfileData(status = combine_profile_status(account.status, "INACTIVE"), _id = profile._id))
        yield event_status_company
    
    
    event = await aggproxy.deactivate_company(cmd.data)
    yield event

# Activate company
@_entity
class ActivateCompany(Command):
    data = field(type=UpdateStatusCompanyData, mandatory=True)
    
    class Meta:
        resource = "company/{id}"
        tags = ["company"]
        description = "Activate company"
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
        
@_handler(ActivateCompany)
async def handle_activate_company(aggproxy, cmd: UpdateStatusCompanyData):
    profile_list = await aggproxy.state.find(
        "profile",
        data_query = {
            "where": {
                "company_id": cmd.aggroot.identifier,
                
            }   
        }
    )
    for profile in profile_list:
        account = await aggproxy.state.fetch(
        "user", profile.account_id
        )
        event_status_company = await aggproxy.update_profile(UpdateProfileData(status = combine_profile_status(account.status, "ACTIVE"), _id = profile._id))
        yield event_status_company
    
    
    event = await aggproxy.activate_company(cmd.data)
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
    event = await aggproxy.update_profile(UpdateProfileData.extend_pclass(
        pclass=cmd.data, _id = cmd.aggroot.identifier
    ))
    
    yield event

# suspend profile
@_entity
class SuspendProfile(Command):
    data = field(type=UpdateStatusProfileData, mandatory=True)
    
    class Meta:
        resource = "profile/{id}"
        tags = ["profile"]
        description = "Suspend profile"
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
        
@_handler(SuspendProfile)
async def handle_suspend_profile(aggproxy, cmd: UpdateStatusProfileData):
    event = await aggproxy.suspend_profile(cmd.data)
    yield event


# active profile

@_entity
class ActiveProfile(Command):
    data = field(type=UpdateStatusProfileData, mandatory=True)
    
    class Meta:
        resource = "profile/{id}"
        tags = ["profile"]
        description = "Active profile"
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
    
@_handler(ActiveProfile)
async def handle_active_profile(aggproxy, cmd: UpdateStatusProfileData):
    event = await aggproxy.active_profile(cmd.data)
    yield event   


# Add user to company role
@_entity("add-companyrole") 
class CreateRole(Command):
    data = field(type=CompanyRoleData)

    class Meta:
        resource = "company-profile"
        tags = ["company-profile"]
        description = "Add user to company role"

@_handler(CreateRole)
async def handle_create_role(aggproxy, cmd: CompanyRoleData):
    
    event = await aggproxy.create_role(cmd.data)
    yield event
    yield aggproxy.create_response(
        "role-response", cmd, {"_id": event.data._id}
    )


# remove user from company role
@_entity
class RemoveRole(Command):
    pass
    
    class Meta:
        resource = "company-profile/{id}"
        tags = ["company-profile"]
        description = "Remove user from company role"
        parameters = [
            {
                "name": "id",
                "in": "path",
                "description": "Company Profile ID: ",
                "required": True,
                "schema": {
                    "type": "string",
                },
            }
        ]
    
@_handler(RemoveRole)
async def handle_remove_role(aggproxy, cmd: RemoveRole):
    event = await aggproxy.remove_role()
    yield event   


