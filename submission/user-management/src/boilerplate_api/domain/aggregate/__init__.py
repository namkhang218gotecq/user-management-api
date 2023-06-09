from .boilerplate import  CardAggregate, UserAggregate, CustomerAggregate,  TransactionrecordAggregate,SystemRoleAggregate, CompanyAggregate


class Aggregate(CardAggregate, UserAggregate, CustomerAggregate,  TransactionrecordAggregate,SystemRoleAggregate, CompanyAggregate):
    pass
