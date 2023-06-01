from sanic_cqrs import register_domain_endpoint

from .command import *  # noqa
from .domain import BoilerplateDomain
from .event import *  # noqa
from .resource import *  # noqa
from .response import *  # noqa


def configure_domain(app):
    register_domain_endpoint(app, BoilerplateDomain)


__all__ = "configure_domain"
