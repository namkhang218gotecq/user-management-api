from sanic_query.resource import register_resource

from boilerplate_api import config
from . import user
from . import system
from . import company
from . import profile
from . import viewProfile
from . import companyinfo
from . import profileStatus
from . import companyStatus
from . import dashboard
from . import companyKind
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
    #Query for dashboard
    register_view(dashboard.DashboardQuery)
    register_view(profileStatus.ProfileStatusQuery)
    register_view(companyStatus.CompanyStatusQuery)
    register_view(companyKind.CompanyKindQuery)
    #Company info 
    register_view(companyinfo.CompanyinfoQuery)
    
