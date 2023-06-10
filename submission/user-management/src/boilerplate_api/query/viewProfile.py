from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class ProfileQueryResource(QueryResource):

    _id = f.UUIDField("ID", identifier=True)
    profile_status = f.StringField("profile_status")
    
    _deleted = f.StringField("Deleted")
    _created = f.StringField("Created")
    _updated = f.StringField("Updated")
    _etag = f.StringField("Etag")
    _creator = f.UUIDField("Creator")
    _updater = f.UUIDField("Updater")

class ProfileQuery(ProfileQueryResource):
    __table__ = "profile_status_view"
    
    class Meta:
        tags = ["profile"]
        description = "get status of profile"
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 