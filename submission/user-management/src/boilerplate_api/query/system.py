from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class SystemQueryResource(QueryResource):

    _id = f.StringField("ID", identifier=True)
    name = f.StringField("name")
    key = f.StringField("key")
    description = f.StringField("description")
    active = f.StringField("active")
    company_kind = f.EnumField("")
    
    _deleted = f.StringField("Deleted")
    _created = f.StringField("Created")
    _updated = f.StringField("Updated")
    _etag = f.StringField("Etag")
    _creator = f.UUIDField("Creator")
    _updater = f.UUIDField("Updater")

class SystemQuery(SystemQueryResource):
    __table__ = "system-role"
    
    class Meta:
        tags = ["system-role"]
        description = "get system role information"
    
