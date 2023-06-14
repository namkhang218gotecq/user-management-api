from sanic_cqrs import (
    PostgresCommandStore,
    PostgresContextStore,
    PostgresEventStore
    
)
from fii_cqrs.backend.gino import PostgresActivityLogger
from sanic_cqrs.domain import GinoDomain

from boilerplate_api import __version__, config
from .aggregate import Aggregate

class BoilerplateDomain(GinoDomain):
    __namespace__ = config.BOILERPLATE_API_DOMAIN
    __aggregate__ = Aggregate
    __revision__ = 1
    __version__ = __version__

    EventStore = PostgresEventStore
    CommandStore = PostgresCommandStore
    ContextStore = PostgresContextStore
    ActivityLogger = PostgresActivityLogger