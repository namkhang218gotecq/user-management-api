from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class CompanyStatusQueryResource(QueryResource):

    type = f.StringField("type", identifier=True, source="status")
    bg_color = f.StringField("bg_color")
    amount = f.StringField("amount")
    

class CompanyStatusQuery(CompanyStatusQueryResource):
    __table__ =  "view--company-status"
    
    class Meta:
        tags = ["query"]
        description = "Company status count"
    
 
 
 
 
 
 
 
 