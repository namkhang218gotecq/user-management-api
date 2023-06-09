from sqlalchemy.dialects.postgresql import UUID

from fii_cqrs.backend.gino import GinoBaseModel, db

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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class CardModel(GinoBaseModel):
    __tablename__ = "card"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)

    _id = db.Column(UUID, primary_key=True)
    password = db.Column(db.String)
    balance = db.Column(db.Float)
    # customer_id = db.Column(
    #     UUID, db.ForeignKey(f"gotecq--khang--atm.customer._id")
    # )





class CustomerModel(GinoBaseModel):
    __tablename__ = "customer"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)

    _id = db.Column(UUID, primary_key=True)
    identity_number = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    address__city = db.Column(db.String)



class TransactionrecordModel(GinoBaseModel):
    __tablename__ = "transaction_record"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)

    _id = db.Column(UUID, primary_key=True)
    card_id = db.Column(
        UUID)
    transaction_type_id = db.Column(
        UUID)
    amount = db.Column(db.Float)
    message = db.Column(db.String)