from sqlalchemy.dialects.postgresql import UUID

from fii_cqrs.backend.gino import GinoBaseModel, db

from boilerplate_api import config


class BoilerplateModel(GinoBaseModel):
    __tablename__ = "boilerplate"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)

    _id = db.Column(UUID, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

class CardModel(GinoBaseModel):
    __tablename__ = "card"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)

    _id = db.Column(UUID, primary_key=True)
    password = db.Column(db.String)
    balance = db.Column(db.Float)
    customer_id = db.Column(
        UUID, db.ForeignKey(f"gotecq--khang--atm.customer._id")
    )



class BankModel(GinoBaseModel):
    __tablename__ = "bank"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)

    _id = db.Column(UUID, primary_key=True)
    bank__name = db.Column(db.String)
    address__line = db.Column(db.String)
    address__city = db.Column(db.String)
    address__state = db.Column(db.String)
    address__country = db.Column(db.String)
    postal__code = db.Column(db.String)
    phone = db.Column(db.String)

class CustomerModel(GinoBaseModel):
    __tablename__ = "customer"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)

    _id = db.Column(UUID, primary_key=True)
    identity_number = db.Column(db.String)
    fist_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    address__city = db.Column(db.String)


class TransactiontypeModel(GinoBaseModel):
    __tablename__ = "transaction_type"
    __table_args__ = dict(schema=config.BOILERPLATE_SCHEMA)

    _id = db.Column(UUID, primary_key=True)
    transaction_type = db.Column(db.String)
    description = db.Column(db.String)

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