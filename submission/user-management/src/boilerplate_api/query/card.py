from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class CardQueryResource(QueryResource):

    _id = f.StringField("ID", identifier=True)
    password = f.StringField("password")
    balance = f.FloatField("balance")
    customer_id = f.StringField("Customer_id")
    
class CardQuery(CardQueryResource):
    __table__ = "card"
    
    class Meta:
        tags = ["Card"]
        description = "get card information"
    



