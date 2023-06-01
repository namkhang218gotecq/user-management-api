from sanic_query import field as f
from sanic_query.resource import QueryResource


class BaseQueryResource(QueryResource):
    __soft_delete__ = "_deleted"

    _id = f.StringField("ID", identifier=True)
    _deleted = f.StringField("Deleted")
    _created = f.StringField("Created")
    _updated = f.StringField("Updated")
    _etag = f.StringField("Etag")
    _creator = f.UUIDField("Creator")
    _updater = f.UUIDField("Updater")


class BoilerplateQuery(BaseQueryResource):
    __table__ = "boilerplate"

    _id = f.StringField("ID", identifier=True)
    name = f.StringField("Name")
    description = f.StringField("Description")

    class Meta:
        tags = ["Boilerplate"]
        description = "Get boilerplate data"

class TransactionTypeQuery(BaseQueryResource):
    __table__ = "transaction_type"
    
    _id = f.StringField("ID", identifier=True)
    transaction_type = f.EnumField("Transaction_type")
    description = f.StringField("Description")

    class Meta:
        tags = ["transactionType"]
        description = "Get transaction type data"


class TransactionRecordQuery(BaseQueryResource):
    __table__ = "transaction_record"
    
    _id = f.StringField("ID", identifier=True)
    card_id = f.UUIDField("Card_id")
    transaction_type_id = f.UUIDField("Transaction_type_id")
    amount = f.FloatField("amount")
    message = f.StringField("Message")
    class Meta:
        tags = ["transactionRecord"]
        description = "Get transaction record data"

