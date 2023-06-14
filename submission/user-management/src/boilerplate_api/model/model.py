from sqlalchemy.dialects.postgresql import UUID

from fii_cqrs.backend.gino import GinoBaseModel, db
from enum import Enum
from boilerplate_api import config


class UserModel(GinoBaseModel):
    __tablename__ = "account"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)

    _id = db.Column(UUID, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    status = db.Column(db.String)
    
class SystemRoleModel(GinoBaseModel):
    __tablename__ = "system-role"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)
    
    _id = db.Column(UUID, primary_key=True)
    name = db.Column(db.String)
    key = db.Column(db.String)
    description = db.Column(db.String)
    active = db.Column(db.String)
    company_kind = db.Column(db.String)
    

class CompanyModel(GinoBaseModel):
    __tablename__ = "company"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)
    
    _id = db.Column(UUID, primary_key=True)
    status = db.Column(db.String)
    kind = db.Column(db.String)
    company_name = db.Column(db.String)
    telecom__email = db.Column(db.String)
    telecom__phone = db.Column(db.String)
    description = db.Column(db.String)
    address__postal = db.Column(db.String)
    address__state = db.Column(db.String)
    address__country = db.Column(db.String)
    tax_id = db.Column(db.String)
    category_name = db.Column(db.String)
    company_code = db.Column(db.String)
    npi = db.Column(db.String)

class StatusEnum(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"
    EXPIRED = "EXPIRED"
    COMPANY_DEACTIVATED = "COMPANY_DEACTIVATED"
    DEACTIVATED = "DEACTIVATED"
    
class ProfileModel(GinoBaseModel):
    __tablename__ = "profile"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)
    
    _id = db.Column(UUID, primary_key=True)
    account_id = db.Column(UUID)
    company_id = db.Column(UUID)
    status = db.Column(db.String)
    name__family = db.Column(db.String)
    name__given = db.Column(db.String)
    telecom__email = db.Column(db.String)
    telecom__phone = db.Column(db.String)
    address__postal = db.Column(db.String)
    address__state = db.Column(db.String)
    address__country = db.Column(db.String)
    address__line = db.Column(db.String)
    gender = db.Column(db.String)
    birth_date = db.Column(db.DateTime)
    name__suffix = db.Column(db.String)
    name__prefix = db.Column(db.String)
    name__middle = db.Column(db.String)
    avatar = db.Column(UUID)
    
class ViewProfileModel(GinoBaseModel):
    __tablename__ = "profile-status-view"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)
    
    _id = db.Column(UUID, primary_key=True)
    profile_status = db.Column(db.String)
    

class StatusProfileModel(GinoBaseModel):
    __tablename__ = "profile-info-view"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)
    _id = db.Column(UUID, primary_key=True)
    
    account_id = db.Column(UUID)
    company_id = db.Column(UUID)
    account_status = db.Column(db.String)
    company_status = db.Column(db.String)
    profile_status = db.Column(db.String)
    
    
# 
class CompanyRoleModel(GinoBaseModel):
    __tablename__ = "company-profile"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)
    
    _id = db.Column(UUID, primary_key=True)
    profile_id = db.Column(UUID)
    company_id = db.Column(UUID)
    role_id = db.Column(UUID)
 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
