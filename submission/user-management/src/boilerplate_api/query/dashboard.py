from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class DashboardQueryResource(QueryResource):

    
    total_companies = f.StringField("total_companies",  identifier=True)
    active_companies = f.StringField("active_companies")
    total_profiles = f.StringField("total_profiles")
    active_profiles = f.StringField("active_profiles")
    
    

class DashboardQuery(DashboardQueryResource):
    __table__ =  "view--dashboard-info"
    
    class Meta:
        tags = ["query"]
        description = "Dashboard information"
    
 
 
 
 
 
 
 
 