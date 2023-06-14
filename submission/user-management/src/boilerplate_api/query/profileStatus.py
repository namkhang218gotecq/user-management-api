from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class ProfileStatusQueryResource(QueryResource):

    type = f.StringField("type", identifier=True)
    bg_color = f.StringField("bg_color")
    amount = f.StringField("amount")
    

class ProfileStatusQuery(ProfileStatusQueryResource):
    __table__ =  "profile-status-count"
    
    class Meta:
        tags = ["query"]
        description = "Profile status count"
    
 
 
 
 
 
 
 
 