from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class ActivityLogQueryResource(QueryResource):

    
    _id = f.UUIDField("_id",  identifier=True)
    logroot__identifier = f.UUIDField("logroot__identifier")
    logroot__resource = f.StringField("logroot__resource")
    logroot__namespace = f.StringField("logroot__namespace")
    domain = f.StringField("domain")
    _created = f.StringField("_created")
    message = f.StringField("message")
    msgtype = f.StringField("msgtype")
    msglabel = f.StringField("msglabel")

class ActivityQuery(ActivityLogQueryResource):
    __table__ =  "activity-log"
    
    class Meta:
        tags = ["query"]
        description = "Log Activity"
    
 
 
 
 
 
 
 
 