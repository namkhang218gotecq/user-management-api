from fii_cqrs.aggregate import Aggregate
from fii_cqrs.event import Event
from fii_cqrs.identifier import UUID_GENR

from boilerplate_api.domain.datadef import   CreateUserData,UpdateUserData,CreateSystemRoleData,CreateCompanyData,UpdateCompanyData, CreateProfileData, UpdateProfileData,UpdateStatusProfileData,UpdateStatusAccountData # noqa
from boilerplate_api.domain.datadef import  CreateUserEventData,UpdateUserEventData, CreateSystemRoleEventData,CreateCompanyEventData, UpdateCompanyEventData, CreateProfileEventData, UpdateProfileEventData, UpdateStatusEventProfile,UpdateStatusAccountEvent,CompanyRoleData,CompanyRoleEventData ,UpdateStatusCompanyEvent,UpdateStatusCompanyData # noqa

from boilerplate_api.model import StatusEnum


# user
class UserAggregate(Aggregate):
    async def do__create_user(
        self, data: CreateUserEventData
    ) -> Event:
        
        return self.create_event(
            "user-created", target=self.aggroot, data=data
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
    async def do__update_user_status(
        self, data: UpdateUserEventData
    ) -> Event:
        user = await self.fetch_aggroot()
        
        return self.create_event(
            "user-updated",
            target=self.aggroot,
            data=UpdateUserEventData.extend_pclass(
                pclass=data
            )
        )
        
# Deactivate account
    async def do__deactivate_account(self, data: UpdateStatusAccountData) -> Event:
        account = await self.fetch_aggroot()

        if account.status == "INACTIVE":
            raise ValueError("Profile hiện tại đã INACTIVE. Vui lòng nhập 1 id account khác.")
        
        return self.create_event(
            "deactivated-account",
            target=self.aggroot, 
            data=UpdateStatusAccountEvent(
                status="INACTIVE",
            )
    )
# Activate account
    async def do__activate_account(self, data: UpdateStatusAccountData) -> Event:
        account = await self.fetch_aggroot()

        if account.status == "ACTIVE":
            raise ValueError("Profile hiện tại đã ACTIVE. Vui lòng nhập 1 id account khác.")
        
        return self.create_event(
            "activated-account",
            target=self.aggroot, 
            data=UpdateStatusAccountEvent(
                status="ACTIVE",
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
        
        return self.create_event(
            "company-created", target=self.aggroot, data=data
        )
        
    async def do__update_company(
        self, data: UpdateCompanyData
    ) -> Event:

        return self.create_event(
            "company-updated",
            target=self.aggroot,
            data=UpdateCompanyEventData.extend_pclass(
                pclass=data
            )
        )
# Deactivate company
    async def do__deactivate_company(self, data: UpdateStatusCompanyData) -> Event:
        company = await self.fetch_aggroot()

        if company.status == "INACTIVE":
            raise ValueError("Company hiện tại đã INACTIVE. Vui lòng nhập 1 id company khác.")
        
        return self.create_event(
            "deactivated-company",
            target=self.aggroot, 
            data=UpdateStatusCompanyEvent(
                status="INACTIVE",
            )
    )
# Activate company
    async def do__activate_company(self, data: UpdateStatusCompanyData) -> Event:
        company = await self.fetch_aggroot()

        if company.status == "ACTIVE":
            raise ValueError("Company hiện tại đã ACTIVE. Vui lòng nhập 1 id company khác.")
        
        return self.create_event(
            "activated-company",
            target=self.aggroot, 
            data=UpdateStatusCompanyEvent(
                status="ACTIVE",
            )
    )

# Create profile

class ProfileAggregate(Aggregate):
    async def do__create_profile(
        self, data: CreateProfileEventData
    ) -> Event:
        
        return self.create_event(
            "profile-created", target=self.aggroot, data=data
        )
    
   
    async def do__update_profile(self, data: UpdateProfileData) -> Event:
        return self.create_event(
            "profile-updated",
            target= {
                "resource": "profile",
                "identifier": data._id
            },
            data=UpdateProfileEventData.extend_pclass(
                pclass=data
            )
        )
    
    async def do__suspend_profile(self, data: UpdateStatusProfileData) -> Event:
        profile = await self.fetch_aggroot()

        if profile.status == "INACTIVE":
            raise ValueError("Profile hiện tại đã INACTIVE. Vui lòng nhập 1 id profile khác.")
        
        return self.create_event(
            "profile-suspended",
            target=self.aggroot, 
            data=UpdateStatusEventProfile(
                status="INACTIVE",
            )
    )
    async def do__active_profile(self, data: UpdateStatusProfileData) -> Event:
        profile = await self.fetch_aggroot()

        if profile.status == "ACTIVE":
            raise ValueError("Profile hiện tại đã ACTIVE. Vui lòng nhập 1 id profile khác.")
        
        return self.create_event(
            "profile-active",
            target=self.aggroot, 
            data=UpdateStatusEventProfile(
                status="ACTIVE",
            )
    )
        

# Add user to company role
class CompanyRoleAggregate(Aggregate):
    async def do__create_role(
        self, data: CompanyRoleData
    ) -> Event:
        event_data = CompanyRoleEventData.extend_pclass(
            pclass=data, _id=UUID_GENR()
        )
        return self.create_event(
            "role-created", target=self.aggroot, data=event_data
        )

    async def do__remove_role(
        self
    )-> Event:
        
        return self.create_event(
            "role-deleted",  target={"resource": self.aggroot.resource, "identifier": self.aggroot.identifier}
        )                       


























































