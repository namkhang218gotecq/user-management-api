from fii_cqrs.command import Command, field
from fii_cqrs.identifier import UUID_GENR

from boilerplate_api.domain.datadef import  CreateUserData, UpdateUserData,CreateSystemRoleData,CreateCompanyData, UpdateCompanyData,CreateProfileData, UpdateProfileData, CreateProfileEventData, UpdateStatusProfileData, UpdateStatusAccountData,CompanyRoleData, CreateUserEventData, UpdateUserEventData,UpdateStatusCompanyData,CreateCompanyEventData, CreateUserEventData, UpdateProfileInfoData
from ..domain import BoilerplateDomain
from .helper import combine_profile_status
_entity = BoilerplateDomain.entity
_handler = BoilerplateDomain.command_handler
from boilerplate_api import __version__, config
from boilerplate_api.model.model import AccountStatus, ProfileStatus, CompanyStatus

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
            pclass=cmd.data, _id=UUID_GENR(), status = AccountStatus.ACTIVE
        )
    
    event = await aggproxy.create_user(event_data)
    yield event
    yield aggproxy.create_response(
        "user-response", cmd, {"_id": event.data._id}
    )
    #log activity
    # yield aggproxy.log_activity(
    #     logroot={
    #         "identifier": cmd.aggroot.identifier,
    #         "resource": cmd.aggroot.resource,
    #         "namespace": config.BOILERPLATE_API_DOMAIN,
    #     },
    #     message=f"create user with telecom__email {event_data.telecom__email}",
    #     msglabel="create-user",
    # )

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
   
    # print("EVENT:"  + str(event))
    # print("EVENT ID:", event._id)
    # print("AGGROOT:", event.aggroot)
    # print("TARGET:", event.target)
    # print("DATA:", event.data)
    # yield aggproxy.log_activity(
    #     logroot={
    #         "identifier": cmd.aggroot.identifier,
    #         "resource": cmd.aggroot.resource,
    #         "namespace": config.BOILERPLATE_API_DOMAIN,
    #     },
    #     message=f"Update user with username: {event.data.username}",
    #     msglabel="update-user",
    # )
# Deactivate account
@_entity
class DeactivateAccount(Command):
    # pass
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
        event_status_user = await aggproxy.update_profile_status(UpdateProfileData(status = combine_profile_status(AccountStatus.INACTIVE, company.status), _id = profile._id))
        yield event_status_user
    
    
    event = await aggproxy.deactivate_account(cmd.data)
    yield event
    
    #log activity
    # account = await aggproxy.state.fetch("user", cmd.aggroot.identifier)
    # username = account.username
    # print("ACCOUNT: " + str(account))
    # yield aggproxy.log_activity(
    #     logroot={
    #         "identifier": cmd.aggroot.identifier,
    #         "resource": cmd.aggroot.resource,
    #         "namespace": config.BOILERPLATE_API_DOMAIN,
    #     },
    #     message=f"Deactivated account: {username}",
    #     msglabel="deactivate-account",
    # )
    
# Activate account
@_entity
class ActivateAccount(Command):
    #pass    
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
# FIX: cmd = entity handler
@_handler(ActivateAccount)
async def handle_activate_account(aggproxy, cmd: ActivateAccount):
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
        event_status_user = await aggproxy.update_profile_status(UpdateProfileData(status = combine_profile_status(AccountStatus.ACTIVE, company.status), _id = profile._id))
        yield event_status_user
    event = await aggproxy.activate_account(cmd.data)
    yield event
    
    # Fetch ra account co _id trung voi identifier, sau do lay ra username de log activity.
    # account = await aggproxy.state.fetch("user", cmd.aggroot.identifier)
    # username = account.username
    
    # yield aggproxy.log_activity(
    #     logroot={
    #         "identifier": cmd.aggroot.identifier,
    #         "resource": cmd.aggroot.resource,
    #         "namespace": config.BOILERPLATE_API_DOMAIN,
    #     },
    #     message=f"Activated account: {username}",
    #     msglabel="activate-account",
    # )

#EXPIRED account 
@_entity
class ExpiredAccount(Command):
    #pass    
    class Meta:
        resource = "user/{id}"
        tags = ["user"]
        description = "Expired account"
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
        
@_handler(ExpiredAccount)
async def handle_expired_account(aggproxy, cmd: ExpiredAccount):
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
        event_status_user = await aggproxy.update_profile_status(UpdateProfileData(status = combine_profile_status(AccountStatus.EXPIRED, company.status), _id = profile._id))
        yield event_status_user
    event = await aggproxy.expired_account(cmd.data)
    yield event

#Pending account 
@_entity
class PendingAccount(Command):
    #pass    
    class Meta:
        resource = "user/{id}"
        tags = ["user"]
        description = "Pending account"
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
        
@_handler(PendingAccount)
async def handle_pending_account(aggproxy, cmd: PendingAccount):
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
        event_status_user = await aggproxy.update_profile_status(UpdateProfileData(status = combine_profile_status(AccountStatus.PENDING, company.status), _id = profile._id))
        yield event_status_user
    event = await aggproxy.pending_account(cmd.data)
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
            pclass=cmd.data, _id=UUID_GENR(), status = CompanyStatus.ACTIVE,
        )
    
    event = await aggproxy.create_company(event_data)
    print("EVENT_DATA: " + str(event_data))
    yield event
    yield aggproxy.create_response(
        "company-response", cmd, {"_id": event.data._id}
    )
    
    yield aggproxy.log_activity(
        logroot={
            "identifier": cmd.aggroot.identifier,
            "resource": cmd.aggroot.resource,
            "namespace": config.BOILERPLATE_API_DOMAIN,
        },
        message=f"create company with company name: {event_data.company_name}",
        msglabel="create-company",
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
async def handle_update_company(aggproxy, cmd: UpdateCompany):
    event = await aggproxy.update_company(cmd.data)
    yield event
    
    # company = await aggproxy.state.fetch("company", cmd.aggroot.identifier)
    # yield aggproxy.log_activity(
    #     logroot={
    #         "identifier": cmd.aggroot.identifier,
    #         "resource": cmd.aggroot.resource,
    #         "namespace": config.BOILERPLATE_API_DOMAIN,
    #     },
    #     message=f"update company with company name: {company.company_name}",
    #     msglabel="update-company",
    # )
    
# Deactivate company
@_entity
class DeactivateCompany(Command):
    
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
        event_status_company = await aggproxy.update_profile_status(
            UpdateProfileData(
                status = combine_profile_status(account.status, CompanyStatus.INACTIVE), 
                _id = profile._id)
            )
        yield event_status_company
    
    
    event = await aggproxy.deactivate_company(cmd.data)
    yield event
    
    #log activity
    company = await aggproxy.state.fetch("company", cmd.aggroot.identifier)
    company_name = company.company_name
    
    yield aggproxy.log_activity(
        logroot={
            "identifier": cmd.aggroot.identifier,
            "resource": cmd.aggroot.resource,
            "namespace": config.BOILERPLATE_API_DOMAIN,
        },
        message=f"Deactivated company: {company_name}",
        msglabel="deactivate-company",
    )


# Activate company
@_entity
class ActivateCompany(Command):
    
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
async def handle_activate_company(aggproxy, cmd: ActivateCompany):
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
        event_status_company = await aggproxy.update_profile_status(
            UpdateProfileData(
                status = combine_profile_status(
                    account.status, CompanyStatus.ACTIVE), _id = profile._id))
        yield event_status_company
    
    
    event = await aggproxy.activate_company(cmd.data)
    yield event

    #log activity
    company = await aggproxy.state.fetch("company", cmd.aggroot.identifier)
    company_name = company.company_name
    
    yield aggproxy.log_activity(
        logroot={
            "identifier": cmd.aggroot.identifier,
            "resource": cmd.aggroot.resource,
            "namespace": config.BOILERPLATE_API_DOMAIN,
        },
        message=f"Activated company: {company_name}",
        msglabel="activate-company",
    )
# SETUP company
@_entity
class SetupCompany(Command):
    
    class Meta:
        resource = "company/{id}"
        tags = ["company"]
        description = "Setup company"
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
        
@_handler(SetupCompany)
async def handle_setup_company(aggproxy, cmd: SetupCompany):
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
        event_status_company = await aggproxy.update_profile_status(
            UpdateProfileData(
                status = combine_profile_status(
                    account.status, CompanyStatus.SETUP), _id = profile._id))
        yield event_status_company
    
    
    event = await aggproxy.setup_company(cmd.data)
    yield event

# Review company
@_entity
class ReviewCompany(Command):
    
    class Meta:
        resource = "company/{id}"
        tags = ["company"]
        description = "Review company"
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
        
@_handler(ReviewCompany)
async def handle_review_company(aggproxy, cmd: ReviewCompany):
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
        event_status_company = await aggproxy.update_profile_status(
            UpdateProfileData(
                status = combine_profile_status(
                    account.status, CompanyStatus.REVIEW), _id = profile._id))
        yield event_status_company
    
    
    event = await aggproxy.review_company(cmd.data)
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
    company = await aggproxy.state.fetch("company", cmd.data.company_id)

    # Check if the telecom__email exists in an account
    existing_account = await aggproxy.state.find_one(
        "user",
        data_query={
            "where": {
                "telecom__email": cmd.data.telecom__email
            }
        }
    )
    
   
    if existing_account:
        account_id = existing_account._id
        account_status = existing_account.status
    else:
        # Create a new account if the telecom__email is not found
        user_data = CreateUserEventData(
            _id=UUID_GENR(),
            telecom__email=cmd.data.telecom__email,
            status=AccountStatus.ACTIVE
        )
        from fii import logger
        logger.warning("Account data -> %s", user_data)
        
        # logger.warning("TELECOM ->" + str(user_data.telecom__email))
        # logger.warning("ID -> " + str(user_data._id))
        
        
        event = await aggproxy.create_user(user_data)
        yield event
        
        account_id = event.data._id
        account_status = AccountStatus.ACTIVE
    
    from fii import logger
    logger.warning("Account ID -> %s", account_id)
    logger.warning("Status -> %s", account_status)
    event_data = CreateProfileEventData.extend_pclass(
        pclass=cmd.data,
        _id=UUID_GENR(),
        status=combine_profile_status(account_status, company.status),
        telecom__email=cmd.data.telecom__email,
        account_id=account_id
    )
    logger.warning("Profile data -> %s", event_data)
     # Check if a profile exists in the company
    existing_profile = await aggproxy.state.find_one(
        "profile",
        data_query={
            "where": {
                "company_id": cmd.data.company_id,
                "account_id": account_id
            }
        }
    )
    
    if existing_profile:
        raise ValueError("A profile already exists for this company.")
    event = await aggproxy.create_profile(event_data)
    yield event
    yield aggproxy.create_response(
        "profile-response", cmd, {"_id": event.data._id}
    )
    
# remove company member
@_entity
class RemoveProfile(Command):
    pass
    
    class Meta:
        resource = "profile/{id}"
        tags = ["profile"]
        description = "Remove company member"
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
    
@_handler(RemoveProfile)
async def handle_remove_profile(aggproxy, cmd: RemoveProfile):
    event = await aggproxy.remove_profile()
    yield event   


# Update profile
@_entity
class UpdateProfile(Command):
    data = field(type=UpdateProfileInfoData, mandatory=True)
    
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
async def handle_update_profile(aggproxy, cmd: UpdateProfileInfoData):
    event = await aggproxy.update_profile(cmd.data)
    yield event

# suspend profile
@_entity
class SuspendProfile(Command):
    pass
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

    #log activity
    # profile = await aggproxy.state.fetch("profile", cmd.aggroot.identifier)
    # account = await aggproxy.state.fetch("user", profile.account_id)
    # username = account.username
    
    # yield aggproxy.log_activity(
    #     logroot={
    #         "identifier": cmd.aggroot.identifier,
    #         "resource": cmd.aggroot.resource,
    #         "namespace": config.BOILERPLATE_API_DOMAIN,
    #     },
    #     message=f"Suspended profile: {username}",
    #     msglabel="suspend-profile",
    # )

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
    
    #log activity
    # profile = await aggproxy.state.fetch("profile", cmd.aggroot.identifier)
    # account = await aggproxy.state.fetch("user", profile.account_id)
    # username = account.username
    
    # yield aggproxy.log_activity(
    #     logroot={
    #         "identifier": cmd.aggroot.identifier,
    #         "resource": cmd.aggroot.resource,
    #         "namespace": config.BOILERPLATE_API_DOMAIN,
    #     },
    #     message=f"Actived profile: {username}",
    #     msglabel="activate-profile",
    # )
    

# Add user to company role
@_entity("add-member-role") 
class CreateRole(Command):
    data = field(type=CompanyRoleData)

    class Meta:
        resource = "company/{id}"
        tags = ["company-profile"]
        description = "Add user to company role"
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
@_handler(CreateRole)
async def handle_create_role(aggproxy, cmd: CompanyRoleData):
    from fii import logger
    logger.warning("Company ID: --> %s", cmd.aggroot.identifier)
    
    #check user exists this role in company ?
    existing_role = await aggproxy.state.find_one(
        "company-profile",
        data_query={
            "where": {
                "company_id": cmd.aggroot.identifier,
                "role_id": cmd.data.role_id,
            }
        }
    )
    if existing_role:
        raise ValueError("The user already has this role in the company.")
    
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


