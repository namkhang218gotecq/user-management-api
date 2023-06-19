from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class OfficialRoleQueryResource(QueryResource):

    company_id =f.UUIDField("company_id")
    profile_id = f.UUIDField("profile_id",identifier=True)
    name__family = f.StringField("name__family")
    name__given = f.StringField("name__given")
    role_name = f.StringField("role_name")
    telecom__email = f.StringField("telecom__email")
    telecom__phone = f.StringField("telecom__phone")
    company_name = f.StringField("company_name")

class OfficialRoleQuery(OfficialRoleQueryResource):
    __table__ =  "view--official-role"
    __endpoint__ = "company/<company_id>/official-role"
    
    class Meta:
        tags = ["query"]
        description = "Show user have official role in company"
        parameters = [
            {
                "name": "company_id",
                "in": "path",
                "description": "Account ID",
                "required": True,
                "schema": {"type": "string"},
            },
        ]
    @classmethod
    def base_query(cls, parsed_query, user=None):
        return {
            "company_id": parsed_query.url_params["company_id"],
        }
 
 
 
 
 
 
 
 