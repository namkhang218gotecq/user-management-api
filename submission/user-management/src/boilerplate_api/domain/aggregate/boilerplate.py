from fii_cqrs.aggregate import Aggregate
from fii_cqrs.event import Event
from fii_cqrs.identifier import UUID_GENR

from boilerplate_api.domain.datadef import  CreateCardData, CreateUserData, CreateCustomerData, CreateTransactionrecordData,UpdateCustomerData,UpdateUserData,CreateSystemRoleData,CreateCompanyData,UpdateCompanyData # noqa
from boilerplate_api.domain.datadef import CreateCardEventData, CreateUserEventData, CreateCustomerEventData, CreateTransactionrecordEventData, CardUpdateEventData, TransferMoneyEventData, UpdateCustomerEventData,UpdateUserEventData, CreateSystemRoleEventData,CreateCompanyEventData, UpdateCompanyEventData  # noqa




# user
class UserAggregate(Aggregate):
    async def do__create_user(
        self, data: CreateUserData
    ) -> Event:
        event_data = CreateUserEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "user-created", target=self.aggroot, data=event_data
        )
        
    async def do__update_user(
        self, data: UpdateUserData
    ) -> Event:
        user = await self.fetch_aggroot()

        updated_user = {
            "username": data.username,
            "password": data.password,
            "status": data.status
        }

        return self.create_event(
            "user-updated",
            target=self.aggroot,
            data=UpdateUserEventData(
                username=updated_user["username"],
                password=updated_user["password"],
                status= updated_user["status"]
            )
        )
#System role

class SystemRoleAggregate(Aggregate):
    async def do__create_system_role(
        self, data: CreateSystemRoleData
    ) -> Event:
        event_data = CreateSystemRoleEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "system-role-created", target=self.aggroot, data=event_data
        )                       

# Create company

class CompanyAggregate(Aggregate):
    async def do__create_company(
        self, data: CreateCompanyData
    ) -> Event:
        event_data = CreateCompanyEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "company-created", target=self.aggroot, data=event_data
        )
        
    async def do__update_company(
        self, data: UpdateCompanyData
    ) -> Event:
        company = await self.fetch_aggroot()

        updated_company = {
            "status": data.status,
            "kind": data.kind,
            "company_name": data.company_name,
            "telecom__email": data.telecom__email,
            "telecom__phone": data.telecom__phone,
            "description": data.description,
            "address__postal": data.address__postal,
            "address__state": data.address__state,
            "address__country": data.address__country,
            "tax_id": data.tax_id,
            "category_name": data.category_name,
            "company_code": data.company_code,
            "npi": data.npi,
        }

        return self.create_event(
            "company-updated",
            target=self.aggroot,
            data=UpdateCompanyEventData(
                status=updated_company["status"],
                kind=updated_company["kind"],
                company_name= updated_company["company_name"],
                telecom__email= updated_company["status"],
                telecom__phone= updated_company["telecom__phone"],
                description= updated_company["description"],
                address__postal= updated_company["address__postal"],
                address__state= updated_company["address__state"],
                address__country= updated_company["address__country"],
                tax_id= updated_company["tax_id"],
                category_name= updated_company["category_name"],
                company_code= updated_company["company_code"],
                npi= updated_company["npi"]
            )
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
        
    async def do__update_customer(
        self, data: UpdateCustomerData
    ) -> Event:
        customer = await self.fetch_aggroot()

        updated_customer = {
            "first_name": data.first_name,
            "last_name": data.last_name
        }

        return self.create_event(
            "customer-updated",
            target=self.aggroot,
            data=UpdateCustomerEventData(
                first_name=updated_customer["first_name"],
                last_name=updated_customer["last_name"]
            )
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