from sanic_query.resource import register_resource

from boilerplate_api import config
from . import boilerplate
from . import card
from . import user
from . import customer
from . import system
def configure_query(app):
    register_view = register_resource(
        app,
        api_endpoint=config.BOILERPLATE_API_ENDPOINT,
        url_prefix=config.BOILERPLATE_API_DOMAIN,
        default_schema=config.BOILERPLATE_SCHEMA,
        auth_decorator=False,
    )

    register_view(card.CardQuery)
    register_view(user.UserQuery)
    register_view(customer.CustomerQuery)
    register_view(boilerplate.TransactionRecordQuery)
    register_view(system.SystemQuery)
    
    
