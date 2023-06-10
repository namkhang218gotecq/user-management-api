from fii_cqrs.command import Command, field

from boilerplate_api.domain.datadef import  CreateCardData, CreateUserData, CreateCustomerData, CreateTransactionrecordData, WithdrawMoneyData, DepositMoneyData, TransferMoneyData,UpdateCustomerData, UpdateUserData,CreateSystemRoleData,CreateCompanyData, UpdateCompanyData,CreateProfileData, UpdateProfileData
from ..domain import BoilerplateDomain

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
    
    event = await aggproxy.create_profile(cmd.data)
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





























#  card
@_entity("create-card") 
class CreateCard(Command):
    data = field(type=CreateCardData)

    class Meta:
        resource = "card"
        tags = ["Card"]
        description = "Create new card"

@_handler(CreateCard)
async def handle_create_card(aggproxy, cmd: CreateCard):
    
    event = await aggproxy.create_card(cmd.data)
    yield event
    yield aggproxy.create_response(
        "card-response", cmd, {"_id": event.data._id}
    )
    
# withdraw
@_entity
class WithdrawMoney(Command):
    data = field(type=WithdrawMoneyData, mandatory=True)
    
    class Meta:
        resource = "card/{id}"
        tags = ["transactionRecord"]
        description = "Withdraw money"
        parameters = [
            {
                "name": "id",
                "in": "path",
                "description": "Card ID: ",
                "required": True,
                "schema": {
                    "type": "string",
                },
            }
        ]
@_handler(WithdrawMoney)
async def handle_withdraw_money(aggproxy, cmd: CreateCard):
    
    event = await aggproxy.withdraw_money(cmd.data)
    yield event
    
    
#deposit
@_entity
class DepositMoney(Command):
    data = field(type=DepositMoneyData, mandatory=True)

    class Meta:
        resource = "card/{id}"
        tags = ["transactionRecord"]
        description = "Deposit money"
        parameters = [
            {
                "name": "id",
                "in": "path",
                "description": "Card ID: ",
                "required": True,
                "schema": {
                    "type": "string",
                },
            }
        ]
@_handler(DepositMoney)
async def handle_withdraw_money(aggproxy, cmd: CreateCard):
    
    event = await aggproxy.deposit_money(cmd.data)
    yield event

#transfer
@_entity
class TransferMoney(Command):
    data = field(type=TransferMoneyData, mandatory=True)

    class Meta:
        resource = "card/{id}"
        tags = ["transactionRecord"]
        description = "Transfer money"
        parameters = [
            {
                "name": "id",
                "in": "path",
                "description": "Card ID: ",
                "required": True,
                "schema": {
                    "type": "string",
                },
            }
        ]
@_handler(TransferMoney)
async def handle_transfer_money(aggproxy, cmd: CreateCard):
    
    event = await aggproxy.transfer_money(cmd.data)
    yield event
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



#  customer
@_entity("create-customer") 
class CreateCustomer(Command):
    data = field(type=CreateCustomerData)

    class Meta:
        resource = "customer"
        tags = ["customer"]
        description = "Create new customer"

@_handler(CreateCustomer)
async def handle_create_customer(aggproxy, cmd: CreateCustomer):
    
    event = await aggproxy.create_customer(cmd.data)
    yield event
    yield aggproxy.create_response(
        "customer-response", cmd, {"_id": event.data._id}
    )

@_entity
class UpdateCustomer(Command):
    data = field(type=UpdateCustomerData, mandatory=True)
    
    class Meta:
        resource = "customer/{id}"
        tags = ["customer"]
        description = "Update customer information"
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


@_handler(UpdateCustomer)
async def handle_update_customer(aggproxy, cmd: CreateCustomer):
    event = await aggproxy.update_customer(cmd.data)
    yield event






#transactionRecord
@_entity("create-transactionrecord") 
class CreateTransactionrecord(Command):
    data = field(type=CreateTransactionrecordData)

    class Meta:
        resource = "transactionrecord"
        tags = ["transactionRecord"]
        description = "Create new transaction record"

@_handler(CreateTransactionrecord)
async def handle_create_transactionrecord(aggproxy, cmd: CreateTransactionrecord):
    
    event = await aggproxy.create_transactionrecord(cmd.data)
    yield event
    yield aggproxy.create_response(
        "transactionrecord-response", cmd, {"_id": event.data._id}
    )
