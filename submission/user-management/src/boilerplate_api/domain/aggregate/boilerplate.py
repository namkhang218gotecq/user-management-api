from boilerplate_api.query import card, customer
from fii_cqrs.aggregate import Aggregate
from fii_cqrs.event import Event
from fii_cqrs.identifier import UUID_GENR

from boilerplate_api.domain.datadef import CreateBoilerplateData, CreateCardData, CreatebankData, CreateCustomerData, CreateTransactiontypeData, CreateTransactionrecordData  # noqa
from boilerplate_api.domain.datadef import CreateBoilerplateEventData,CreateCardEventData, CreateBankEventData, CreateCustomerEventData, CreateTransactiontypeEventData, CreateTransactionrecordEventData, CardUpdateEventData, TransferMoneyEventData  # noqa


class BoilerplateAggregate(Aggregate):
    async def do__create_boilerplate(
        self, data: CreateBoilerplateData
    ) -> Event:
        event_data = CreateBoilerplateEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "boilerplate-created", target=self.aggroot, data=event_data
        )
        
# Card
class CardAggregate(Aggregate):
    async def do__create_card(
        self, data: CreateCardData
    ) -> Event:
        event_data = CreateCardEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "card-created", target=self.aggroot, data=event_data
        )
        
# Bank
class BankAggregate(Aggregate):
    async def do__create_bank(
        self, data: CreatebankData
    ) -> Event:
        event_data = CreateBankEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "bank-created", target=self.aggroot, data=event_data
        )

# Customer
class CustomerAggregate(Aggregate):
    async def do__create_customer(
        self, data: CreateCustomerData
    ) -> Event:
        event_data = CreateCustomerEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "customer-created", target=self.aggroot, data=event_data
        )

# TransactionType
class TransactiontypeAggregate(Aggregate):
    async def do__create_transactiontype(
        self, data: CreateTransactiontypeData
    ) -> Event:
        event_data = CreateTransactiontypeEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "transactiontype-created", target=self.aggroot, data=event_data
        )

# TransactionRecord
class TransactionrecordAggregate(Aggregate):
    async def do__create_transactionrecord(
        self, data: CreateTransactionrecordData
    ) -> Event:
        event_data = CreateTransactionrecordEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "transactionrecord-created", target=self.aggroot, data=event_data
        )
        
    async def do__withdraw_money(self, data) -> Event:
        card = await self.fetch_aggroot()
        if card.balance < data.amount:
            raise ValueError("You dont have enough money to withdraw")

        new_balance = card.balance - data.amount
        
        from fii import logger
        logger.warning("New Balance: %s", new_balance)
        
        return self.create_event(
            "card-updated",
            target=self.aggroot,
            data=CardUpdateEventData(
                balance = new_balance
                )
        )
    
    async def do__deposit_money(self, data) -> Event:
        card = await self.fetch_aggroot()
        new_balance = card.balance + data.amount
        
        return self.create_event(
            "card-updated",
            target=self.aggroot,
            data=CardUpdateEventData(
                balance = new_balance
            )
        )
        
    async def do__transfer_money(self, data):
        card = await self.fetch_aggroot()
        if card.balance < data.amount:
            raise ValueError("You dont have enough money to transfer")

        return self.create_event(
            "money-transferred",
            target=self.aggroot,
            data= TransferMoneyEventData(
                source_card_id =  self.aggroot.identifier,
                destination_card_id = data.destination_card_id,
                amount =  data.amount
            )
        )