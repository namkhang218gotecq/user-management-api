from fii_cqrs.command import Command, field

from boilerplate_api.domain.datadef import CreateBoilerplateData, CreateCardData, CreatebankData, CreateCustomerData, CreateTransactiontypeData, CreateTransactionrecordData, WithdrawMoneyData, DepositMoneyData, TransferMoneyData
from ..domain import BoilerplateDomain

_entity = BoilerplateDomain.entity
_handler = BoilerplateDomain.command_handler


@_entity("create-boilerplate")
class CreateBoilerplate(Command):
    data = field(type=CreateBoilerplateData)

    class Meta:
        resource = "boilerplate"
        tags = ["boilerplate"]
        description = "Create new boilerplate"


@_handler(CreateBoilerplate)
async def handle_create_boilerplate(aggproxy, cmd: CreateBoilerplate):
    from fii import logger
    logger.warning("================================")
    event = await aggproxy.create_boilerplate(cmd.data)
    yield event
    yield aggproxy.create_response(
        "boilerplate-response", cmd, {"_id": event.data._id}
    )
    

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
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#  bank
@_entity("create-bank") 
class CreateBank(Command):
    data = field(type=CreatebankData)

    class Meta:
        resource = "bank"
        tags = ["bank Command"]
        description = "Create new bank"

@_handler(CreateBank)
async def handle_create_bank(aggproxy, cmd: CreateBank):
    
    event = await aggproxy.create_bank(cmd.data)
    yield event
    yield aggproxy.create_response(
        "bank-response", cmd, {"_id": event.data._id}
    )

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

#transactionType
@_entity("create-transactiontype") 
class CreateTransactiontype(Command):
    data = field(type=CreateTransactiontypeData)

    class Meta:
        resource = "transactiontype"
        tags = ["transactionType"]
        description = "Create new transaction type"

@_handler(CreateTransactiontype)
async def handle_create_transactiontype(aggproxy, cmd: CreateTransactiontype):
    
    event = await aggproxy.create_transactiontype(cmd.data)
    yield event
    yield aggproxy.create_response(
        "transactiontype-response", cmd, {"_id": event.data._id}
    )

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
