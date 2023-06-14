from sanic_query.resource import register_resource

from boilerplate_api import config
from . import user
from . import system
from . import company
from . import profile
from . import viewProfile
from . import companyinfo
def configure_query(app):
    register_view = register_resource(
        app,
        api_endpoint=config.BOILERPLATE_API_ENDPOINT,
        url_prefix=config.BOILERPLATE_API_DOMAIN,
        default_schema=config.BOILERPLATE_SCHEMA,
        auth_decorator=False,
    )

    register_view(user.UserQuery)
    register_view(system.SystemQuery)
    register_view(company.CompanyQuery)
    register_view(profile.ProfileQuery)
    register_view(viewProfile.ProfileQuery)
    register_view(companyinfo.CompanyinfoQuery)
    
