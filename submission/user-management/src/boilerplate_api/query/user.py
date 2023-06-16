from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class UserQueryResource(QueryResource):

    _id = f.StringField("ID", identifier=True)
    telecom__email = f.StringField("telecom__email")
    password = f.StringField("password")
    status = f.EnumField("")
    _deleted = f.StringField("Deleted")
    _created = f.StringField("Created")
    _updated = f.StringField("Updated")
    _etag = f.StringField("Etag")
    _creator = f.UUIDField("Creator")
    _updater = f.UUIDField("Updater")

class UserQuery(UserQueryResource):
    __table__ = "account"
    
    class Meta:
        tags = ["user"]
        description = "get user information"
    
