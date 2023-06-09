from pydoc import describe
from sanic_query import field as f
from sanic_query.resource import QueryResource

class CompanyQueryResource(QueryResource):

    _id = f.StringField("ID", identifier=True)
    status = f.EnumField("")
    kind = f.StringField("kind")
    company_name = f.StringField("company_name")
    telecom__email = f.StringField("telecom__email")
    telecom__phone = f.StringField("telecom__phone")
    description = f.StringField("description")
    address__postal = f.StringField("address__postal")
    address__state = f.StringField("address__state")
    address__country = f.StringField("address__country")
    tax_id = f.StringField("tax_id")
    category_name = f.StringField("category_name")
    company_code = f.StringField("company_code")
    npi = f.StringField("npi")
    
    _deleted = f.StringField("Deleted")
    _created = f.StringField("Created")
    _updated = f.StringField("Updated")
    _etag = f.StringField("Etag")
    _creator = f.UUIDField("Creator")
    _updater = f.UUIDField("Updater")

class CompanyQuery(CompanyQueryResource):
    __table__ = "company"
    
    class Meta:
        tags = ["company"]
        description = "Get company information"
    
