from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class UserInfoQueryResource(QueryResource):
    
    _id = f.StringField("_id", identifier=True)
    
    profile_id = f.StringField("profile_id")
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
    __table__ =  "view--user-info"
    __endpoint__ = "account/<account_id>/profile"
    
    class Meta:
        tags = ["query"]
        description = "User Info"
        parameters = [
            {
                "name": "account_id",
                "in": "path",
                "description": "Account ID",
                "required": True,
                "schema": {"type": "string"},
            },
        ]
    # @classmethod
    # def base_query(cls, parsed_query, user=None):
    #     return {
    #         "account_id": parsed_query.url_params["account_id"],
    #     }
        
#  57341d6d-24dd-48fc-a61d-f678f459f238
#  6daab2b4-40f0-4f11-967a-c5d0e8192097