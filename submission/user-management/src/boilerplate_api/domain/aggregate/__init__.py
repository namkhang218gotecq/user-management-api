from .boilerplate import  CardAggregate, UserAggregate, CustomerAggregate,  TransactionrecordAggregate,SystemRoleAggregate


class Aggregate(CardAggregate, UserAggregate, CustomerAggregate,  TransactionrecordAggregate,SystemRoleAggregate):
    pass
