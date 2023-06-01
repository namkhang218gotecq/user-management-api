from sanic_cqrs.helper import create_app
from sanic_kcauth import configure_kcauth

import boilerplate_api
from boilerplate_api.domain import configure_domain
from boilerplate_api.query import configure_query

app = create_app(boilerplate_api)

configure_kcauth(app)
configure_domain(app)
configure_query(app)
