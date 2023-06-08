from pydoc import describe
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


class CustomerQuery(BaseQueryResource):
    __table__ = "customer"
    
    _id = f.StringField("ID", identifier=True)
    identity_number = f.StringField("identity_number")
    first_name = f.StringField("first_name")
    last_name = f.StringField("last_name")
    phone = f.StringField("phone")
    address__city = f.StringField("address__city")
    class Meta:
        tags = ["customer"]
        description = "get customer information"
    
