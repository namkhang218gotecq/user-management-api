from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class UserInfoQueryResource(QueryResource):

    
    account_id = f.UUIDField("account_id",  identifier=True)
    profile_id = f.UUIDField("profile_id")
    account_username = f.StringField("account_username")
    name__family = f.StringField("name__family")
    name__given = f.StringField("name__given")
    telecom__email = f.StringField("telecom__email")
    telecom__phone = f.StringField("telecom__phone")
    address__postal = f.StringField("address__postal")
    address__state = f.StringField("address__state")
    address__country = f.StringField("address__country")
    address__line = f.StringField("address__line")
    gender = f.StringField("gender")
    name__prefix = f.StringField("name__prefix")
    name__suffix = f.StringField("name__suffix")
    name__middle = f.StringField("name__middle")

  

class UserinfoQuery(UserInfoQueryResource):
    __table__ =  "user-info-view"
    
    class Meta:
        tags = ["query"]
        description = "User Info"
    
 
 
 
 
 
 
 
 