from fii_cqrs.aggregate import Aggregate
from fii_cqrs.event import Event
from fii_cqrs.identifier import UUID_GENR

from boilerplate_api.domain.datadef import   CreateUserData,UpdateUserData,CreateSystemRoleData,CreateCompanyData,UpdateCompanyData, CreateProfileData, UpdateProfileData,UpdateStatusProfileData # noqa
from boilerplate_api.domain.datadef import  CreateUserEventData,UpdateUserEventData, CreateSystemRoleEventData,CreateCompanyEventData, UpdateCompanyEventData, CreateProfileEventData, UpdateProfileEventData, UpdateStatusEventProfile  # noqa

from boilerplate_api.model import StatusEnum


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

        return self.create_event(
            "company-updated",
            target=self.aggroot,
            data=UpdateCompanyEventData.extend_pclass(
                pclass=data
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
            target=self.aggroot,
            data=UpdateProfileEventData.extend_pclass(
                pclass=data
            )
        )
    
    async def do__suspend_profile(self, data: UpdateStatusProfileData) -> Event:
        profile = await self.fetch_aggroot()

        return self.create_event(
            "profile-suspended",
            target=self.aggroot, 
            data=UpdateStatusEventProfile(
                status = "INACTIVE",
            )
        )































































