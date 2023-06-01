from sanic_query.resource import register_resource

from boilerplate_api import config
from . import boilerplate
from . import card
from . import bank
from . import customer
def configure_query(app):
    register_view = register_resource(
        app,
        api_endpoint=config.BOILERPLATE_API_ENDPOINT,
        url_prefix=config.BOILERPLATE_API_DOMAIN,
        default_schema=config.BOILERPLATE_SCHEMA,
        auth_decorator=False,
    )

    register_view(boilerplate.BoilerplateQuery)
    register_view(card.CardQuery)
    register_view(bank.BankQuery)
    register_view(customer.CustomerQuery)
    register_view(boilerplate.TransactionTypeQuery)
    register_view(boilerplate.TransactionRecordQuery)
    
    
