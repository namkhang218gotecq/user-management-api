from fii_cqrs.aggregate import Aggregate
from fii_cqrs.event import Event
from fii_cqrs.identifier import UUID_GENR

from boilerplate_api.domain.datadef import   CreateUserData,UpdateUserData,CreateSystemRoleData,CreateCompanyData,UpdateCompanyData, CreateProfileData, UpdateProfileData # noqa
from boilerplate_api.domain.datadef import  CreateUserEventData,UpdateUserEventData, CreateSystemRoleEventData,CreateCompanyEventData, UpdateCompanyEventData, CreateProfileEventData, UpdateProfileEventData  # noqa




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

# Create profile

class ProfileAggregate(Aggregate):
    async def do__create_profile(
        self, data: CreateProfileData
    ) -> Event:
        event_data = CreateProfileEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "profile-created", target=self.aggroot, data=event_data
        )
    

    async def do__update_profile(self, data: UpdateProfileData) -> Event:
        profile = await self.fetch_aggroot()

        # account_obj = await self.fetch_rootobj("user", profile.account_id)
        # account_status = account_obj.status

        # company_obj = await self.fetch_rootobj("company", profile.company_id)
        # company_status = company_obj.status
    
        # profile_status = self.combine_profile_status(account_status, company_status)

        updated_profile = {
            "status": data.status,
            "name__family": data.name__family,
            "name__given": data.name__given,
            "telecom__email": data.telecom__email,
            "telecom__phone": data.telecom__phone,
            "address__postal": data.address__postal,
            "address__state": data.address__state,
            "address__country": data.address__country,
            "address__line": data.address__line,
            "gender": data.gender,
            "birth_date": data.birth_date,
            "name__suffix": data.name__suffix,
            "name__prefix": data.name__prefix,
            "name__middle": data.name__middle,
            "avatar": data.avatar,
        }

        return self.create_event(
            "profile-updated",
            target=self.aggroot,
            data=UpdateProfileEventData(
                status=updated_profile["status"],
                name__family=updated_profile["name__family"],
                name__given=updated_profile["name__given"],
                telecom__email=updated_profile["telecom__email"],
                telecom__phone=updated_profile["telecom__phone"],
                address__postal=updated_profile["address__postal"],
                address__state=updated_profile["address__state"],
                address__country=updated_profile["address__country"],
                address__line=updated_profile["address__line"],
                gender=updated_profile["gender"],
                birth_date=updated_profile["birth_date"],
                name__suffix=updated_profile["name__suffix"],
                name__prefix=updated_profile["name__prefix"],
                name__middle=updated_profile["name__middle"],
                avatar=updated_profile["avatar"]
            )
        )

































































