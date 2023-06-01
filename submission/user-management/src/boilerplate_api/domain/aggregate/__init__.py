from .boilerplate import BoilerplateAggregate, CardAggregate, BankAggregate, CustomerAggregate, TransactiontypeAggregate, TransactionrecordAggregate


class Aggregate(BoilerplateAggregate, CardAggregate, BankAggregate, CustomerAggregate, TransactiontypeAggregate, TransactionrecordAggregate):
    pass
