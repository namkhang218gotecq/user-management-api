from fii_cqrs import identifier
from fii_cqrs.event import Event, field
from fii_cqrs.state import InsertRecord

from boilerplate_api.domain.datadef import  CreateCardEventData,CreateUserEventData, CreateCustomerEventData, CreateTransactionrecordEventData, CardUpdateEventData, TransferMoneyEventData, UpdateCustomerEventData,UpdateUserEventData,CreateSystemRoleEventData, CreateCompanyEventData, UpdateCompanyEventData, CreateProfileEventData, UpdateProfileEventData, UpdateStatusEventProfile
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

#Update status profile
@_entity('profilestatus-updated')
class StatusProfileUpdated(Event):
    data = field(type=UpdateStatusEventProfile, mandatory=True)

@_committer(StatusProfileUpdated)
async def process__profilestatus_updated(statemgr, event):
    yield UpdateRecord(
        resource=event.target.resource, 
        data=event.data, 
        identifier=event.target.identifier)








































#----------------------------------------------------------------

@_entity
class CardCreated(Event):
    data = field(type=CreateCardEventData, mandatory=True)


@_committer(CardCreated)
async def process__card_created(statemgr, event):
    yield InsertRecord(resource=event.target.resource, data=event.data)
    
@_entity
class CustomerCreated(Event):
    data = field(type=CreateCustomerEventData, mandatory=True)


@_committer(CustomerCreated)
async def process__customer_created(statemgr, event):
    yield InsertRecord(resource=event.target.resource, data=event.data)
    
#----------------------------------------------------------------


@_entity
class TransactionrecordCreated(Event):
    data = field(type=CreateTransactionrecordEventData, mandatory=True)


@_committer(TransactionrecordCreated)
async def process__Transactionrecord_created(statemgr, event):
    yield InsertRecord(resource=event.target.resource, data=event.data)
    

@_entity('card-updated')
class CardUpdated(Event):
    data = field(type=CardUpdateEventData, mandatory=True)

@_committer(CardUpdated)
async def process__card_updated(statemgr, event):
    from fii import logger
    logger.warning("New Balance: %s", event.data)
    
    yield UpdateRecord(
        resource=event.target.resource, 
        data=event.data, 
        identifier=event.target.identifier)

@_entity('money-transferred')
class MoneyTransferred(Event):
    data = field(type=TransferMoneyEventData, mandatory=True)

@_committer(MoneyTransferred)
async def process__money_transferred(statemgr, event):
    from fii import logger
    logger.warning("New Balance: %s", event.data)
    
    source_card = await statemgr.fetch(
        resource=event.target.resource,
        _id=event.data.source_card_id
    )
    
    new_balance = source_card.balance - event.data.amount
    yield UpdateRecord(
        resource=event.target.resource, #table
        data=CardUpdateEventData(
            balance = new_balance), 
        identifier=event.target.identifier #id record 
    )
    
    destination_card = await statemgr.fetch(
        resource=event.target.resource,
        _id=event.data.destination_card_id
    )
    
    recipient_new_balance = destination_card.balance + event.data.amount
    from fii import logger
    logger.warning("New Target: %s", event.target)
    yield UpdateRecord(
        resource=event.target.resource, 
        data=CardUpdateEventData(
            balance = recipient_new_balance), 
        identifier = destination_card._id
    )

@_entity('customer-updated')
class CustomerUpdated(Event):
    data = field(type=UpdateCustomerEventData, mandatory=True)

@_committer(CustomerUpdated)
async def process__customer_updated(statemgr, event):
    from fii import logger
    logger.warning("New DATA: %s", event.data)
    
    yield UpdateRecord(
        resource=event.target.resource, 
        data=event.data, 
        identifier=event.target.identifier)