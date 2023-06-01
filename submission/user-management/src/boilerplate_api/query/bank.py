from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class BankQueryResource(QueryResource):

    _id = f.StringField("ID", identifier=True)
    bank__name = f.StringField("bank__name")
    address__line = f.StringField("address__line")
    address__city = f.StringField("address__city")
    address__state = f.StringField("address__state")
    address__country = f.StringField("address__country")
    postal__code = f.StringField("postal__code")
    phone = f.StringField("phone")

class BankQuery(BankQueryResource):
    __table__ = "bank"
    
    class Meta:
        tags = ["bank"]
        description = "get bank information"
    
