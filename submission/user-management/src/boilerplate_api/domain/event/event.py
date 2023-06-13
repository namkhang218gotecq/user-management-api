from fii_cqrs import identifier
from fii_cqrs.event import Event, field
from fii_cqrs.state import InsertRecord

from boilerplate_api.domain.datadef import  CreateUserEventData,UpdateUserEventData,CreateSystemRoleEventData, CreateCompanyEventData, UpdateCompanyEventData, CreateProfileEventData, UpdateProfileEventData, UpdateStatusEventProfile,UpdateStatusAccountEvent,CompanyRoleEventData
from fii_cqrs.statemut import GenericStateMutation, UpdateRecord
from ..domain import BoilerplateDomain

_entity = BoilerplateDomain.entity
_committer = BoilerplateDomain.event_committer

#User
@_entity
class UserCreated(Event):
    data = field(type=CreateUserEventData, mandatory=True)


@_committer(UserCreated)
async def process__user_created(statemgr, event):
    yield InsertRecord(resource=event.target.resource, data=event.data)
    
#Update user
@_entity('user-updated')
class UserUpdated(Event):
    data = field(type=UpdateUserEventData, mandatory=True)

@_committer(UserUpdated)
async def process__customer_updated(statemgr, event):
    from fii import logger
    logger.warning("UPDATE USER: %s", event.data) #User input data
    logger.warning("LOG RESOURCE: %s", event.target.resource) #resource name -> table 
    logger.warning("LOG identifier: %s", event.target.identifier) #id record
    
    yield UpdateRecord(
        resource=event.target.resource, 
        data=event.data, 
        identifier=event.target.identifier)

# deactivate account

@_entity('deactivated-account')
class DeactivateAccount(Event):
    data = field(type=UpdateStatusAccountEvent, mandatory=True)

@_committer(DeactivateAccount)
async def process__deactivate_account(statemgr, event):
    yield UpdateRecord(
        resource=event.target.resource, 
        data=event.data, 
        identifier=event.target.identifier
    )
    
# activate account

@_entity('activated-account')
class ActivateAccount(Event):
    data = field(type=UpdateStatusAccountEvent, mandatory=True)

@_committer(ActivateAccount)
async def process__activate_account(statemgr, event):
    yield UpdateRecord(
        resource=event.target.resource, 
        data=event.data, 
        identifier=event.target.identifier
    )


#Create System role
@_entity
class SystemRoleCreated(Event):
    data = field(type=CreateSystemRoleEventData, mandatory=True)


@_committer(SystemRoleCreated)
async def process__system_role_created(statemgr, event):
    yield InsertRecord(resource=event.target.resource, data=event.data)

#Create company
@_entity
class CompanyCreated(Event):
    data = field(type=CreateCompanyEventData, mandatory=True)


@_committer(CompanyCreated)
async def process__company_created(statemgr, event):
    yield InsertRecord(resource=event.target.resource, data=event.data)


#Update company
@_entity('company-updated')
class ComapnyUpdated(Event):
    data = field(type=UpdateCompanyEventData, mandatory=True)

@_committer(ComapnyUpdated)
async def process__company_updated(statemgr, event):
    yield UpdateRecord(
        resource=event.target.resource, 
        data=event.data, 
        identifier=event.target.identifier)


#Create profile
@_entity
class ProfileCreated(Event):
    data = field(type=CreateProfileEventData, mandatory=True)


@_committer(ProfileCreated)
async def process__profile_created(statemgr, event):
    yield InsertRecord(resource=event.target.resource, data=event.data)


#Update profile
@_entity('profile-updated')
class ProfileUpdated(Event):
    data = field(type=UpdateProfileEventData, mandatory=True)

@_committer(ProfileUpdated)
async def process__profile_updated(statemgr, event):
    yield UpdateRecord(
        resource=event.target.resource, 
        data=event.data, 
        identifier=event.target.identifier)

#suspend profile
@_entity('profile-suspended')
class ProfileSuspended(Event):
    data = field(type=UpdateStatusEventProfile, mandatory=True)

@_committer(ProfileSuspended)
async def process__suspend_profile(statemgr, event):
    yield UpdateRecord(
        resource=event.target.resource, 
        data=event.data, 
        identifier=event.target.identifier)


@_entity('profile-active')
class ProfileActive(Event):
    data = field(type=UpdateStatusEventProfile, mandatory=True)

@_committer(ProfileActive)
async def process__active_profile(statemgr, event):
    yield UpdateRecord(
        resource=event.target.resource, 
        data=event.data, 
        identifier=event.target.identifier)

@_entity
class CompanyDeactivated(Event):
    company_id = field(type=str, mandatory=True)




#Role
@_entity
class RoleCreated(Event):
    data = field(type=CompanyRoleEventData, mandatory=True)


@_committer(RoleCreated)
async def process__create_role(statemgr, event):
    yield InsertRecord(resource=event.target.resource, data=event.data)
    


























