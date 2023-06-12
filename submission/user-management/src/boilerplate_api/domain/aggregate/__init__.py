from .aggregate import   UserAggregate,SystemRoleAggregate, CompanyAggregate, ProfileAggregate


class Aggregate( UserAggregate, SystemRoleAggregate, CompanyAggregate, ProfileAggregate):
    pass
