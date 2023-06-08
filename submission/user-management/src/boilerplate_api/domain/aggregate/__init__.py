from .boilerplate import  CardAggregate, UserAggregate, CustomerAggregate, TransactiontypeAggregate, TransactionrecordAggregate


class Aggregate(CardAggregate, UserAggregate, CustomerAggregate, TransactiontypeAggregate, TransactionrecordAggregate):
    pass
