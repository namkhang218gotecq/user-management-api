from sanic_query import field as f
from sanic_query.resource import QueryResource


class BaseQueryResource(QueryResource):
    __soft_delete__ = "_deleted"

    _id = f.StringField("ID", identifier=True)
    _deleted = f.StringField("Deleted")
    _created = f.StringField("Created")
    _updated = f.StringField("Updated")
    _etag = f.StringField("Etag")
    _creator = f.UUIDField("Creator")
    _updater = f.UUIDField("Updater")



