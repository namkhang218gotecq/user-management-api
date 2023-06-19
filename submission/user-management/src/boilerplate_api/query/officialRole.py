from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class OfficialRoleQueryResource(QueryResource):

    company_id =f.UUIDField("company_id", identifier=True)
    profile_id = f.UUIDField("profile_id")
    name__family = f.StringField("name__family")
    name__given = f.StringField("name__given")
    role_name = f.StringField("role_name")
    telecom__email = f.StringField("telecom__email")
    telecom__phone = f.StringField("telecom__phone")
    company_name = f.StringField("company_name")

class OfficialRoleQuery(OfficialRoleQueryResource):
    __table__ =  "view--official-role"
    
    class Meta:
        tags = ["query"]
        description = "Show user have official role in company"
    
 
 
 
 
 
 
 
 