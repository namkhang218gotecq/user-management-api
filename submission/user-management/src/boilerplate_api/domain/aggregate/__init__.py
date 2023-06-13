from .aggregate import   UserAggregate,SystemRoleAggregate, CompanyAggregate, ProfileAggregate,CompanyRoleAggregate

class Aggregate( UserAggregate, SystemRoleAggregate, CompanyAggregate, ProfileAggregate,CompanyRoleAggregate):
    pass
