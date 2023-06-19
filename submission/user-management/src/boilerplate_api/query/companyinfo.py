from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class CompanyInfoQueryResource(QueryResource):

    
    company_id = f.UUIDField("company_id",  identifier=True)
    profile_id = f.UUIDField("profile_id")
    company_name = f.StringField("company_name")
    name__family = f.StringField("name__family")
    name__given = f.StringField("name__given")
    telecom__email = f.StringField("telecom__email")
    name__prefix = f.StringField("name__prefix")
    name__suffix = f.StringField("name__suffix")
    role_name = f.StringField("role_name")
    role_key = f.StringField("role_key")
    role_description = f.StringField("role_description")
    
    _deleted = f.StringField("Deleted")
    _created = f.StringField("Created")
    _updated = f.StringField("Updated")
    _etag = f.StringField("Etag")
    _creator = f.UUIDField("Creator")
    _updater = f.UUIDField("Updater")

class CompanyinfoQuery(CompanyInfoQueryResource):
    __table__ =  "view--company-info"
    
    class Meta:
        tags = ["query"]
        description = "Company info (Show users + role in these company)"
    
 
 
 
 
 
 
 
 