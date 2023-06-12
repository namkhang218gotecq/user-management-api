from .aggregate import  CardAggregate, UserAggregate, CustomerAggregate,  TransactionrecordAggregate,SystemRoleAggregate, CompanyAggregate, ProfileAggregate


class Aggregate(CardAggregate, UserAggregate, CustomerAggregate,  TransactionrecordAggregate,SystemRoleAggregate, CompanyAggregate, ProfileAggregate):
    pass
