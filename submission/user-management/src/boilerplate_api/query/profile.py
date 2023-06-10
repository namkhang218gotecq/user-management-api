from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class ProfileQueryResource(QueryResource):

    _id = f.UUIDField("ID", identifier=True)
    account_id = f.UUIDField("account_id")
    company_id = f.UUIDField("company_id")
    status = f.StringField("status")
    name__family = f.StringField("name__family")
    name__given = f.StringField("name__given")
    telecom__email = f.StringField("telecom__email")
    telecom__phone = f.StringField("telecom__phone")
    address__postal = f.StringField("address__postal")
    address__state = f.StringField("address__state")
    address__country = f.StringField("address__country")
    address__line = f.StringField("address__line")
    gender = f.StringField("gender")
    birth_date = f.DateField("birth_date")
    name__suffix = f.StringField("name__suffix")
    name__prefix = f.StringField("name__prefix")
    name__middle = f.StringField("name__middle")
    avatar = f.UUIDField("avatar")
    
    _deleted = f.StringField("Deleted")
    _created = f.StringField("Created")
    _updated = f.StringField("Updated")
    _etag = f.StringField("Etag")
    _creator = f.UUIDField("Creator")
    _updater = f.UUIDField("Updater")

class ProfileQuery(ProfileQueryResource):
    __table__ = "profile"
    
    class Meta:
        tags = ["profile"]
        description = "get profile information"
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 