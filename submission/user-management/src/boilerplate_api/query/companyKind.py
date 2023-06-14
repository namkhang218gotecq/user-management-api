from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class CompanyKindQueryResource(QueryResource):

    type = f.StringField("type", identifier=True)
    bg_color = f.StringField("bg_color")
    amount = f.StringField("amount")
    

class CompanyKindQuery(CompanyKindQueryResource):
    __table__ =  "company-kind-count"
    
    class Meta:
        tags = ["query"]
        description = "Company kind count"
    
 
 
 
 
 
 
 
 