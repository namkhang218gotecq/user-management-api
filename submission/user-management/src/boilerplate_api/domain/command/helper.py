
from boilerplate_api.model.model import AccountStatus,CompanyStatus,ProfileStatus


def combine_profile_status(account_status, company_status) -> str:
    from fii import logger
    logger.warning("Account status --> %s", account_status)
    logger.warning("Company status --> %s", company_status)
    status_mapping = {
        (AccountStatus.ACTIVE, CompanyStatus.SETUP): ProfileStatus.ACTIVE,
        (AccountStatus.ACTIVE, CompanyStatus.REVIEW): ProfileStatus.ACTIVE,
        (AccountStatus.ACTIVE, CompanyStatus.INACTIVE): ProfileStatus.COMPANY_DEACTIVATED,
        (AccountStatus.ACTIVE, CompanyStatus.ACTIVE): ProfileStatus.ACTIVE,
        
        (AccountStatus.INACTIVE, CompanyStatus.SETUP): ProfileStatus.INACTIVE,
        (AccountStatus.INACTIVE, CompanyStatus.REVIEW): ProfileStatus.INACTIVE,
        (AccountStatus.INACTIVE, CompanyStatus.INACTIVE): ProfileStatus.DEACTIVATED,
        (AccountStatus.INACTIVE, CompanyStatus.ACTIVE): ProfileStatus.DEACTIVATED,
        
        (AccountStatus.EXPIRED, CompanyStatus.SETUP): ProfileStatus.EXPIRED,
        (AccountStatus.EXPIRED, CompanyStatus.REVIEW): ProfileStatus.EXPIRED,
        (AccountStatus.EXPIRED, CompanyStatus.INACTIVE): ProfileStatus.EXPIRED,
        (AccountStatus.EXPIRED, CompanyStatus.ACTIVE): ProfileStatus.EXPIRED,
        
        (AccountStatus.PENDING, CompanyStatus.SETUP): ProfileStatus.PENDING,
        (AccountStatus.PENDING, CompanyStatus.REVIEW): ProfileStatus.PENDING,
        (AccountStatus.PENDING, CompanyStatus.INACTIVE): ProfileStatus.COMPANY_DEACTIVATED,
        (AccountStatus.PENDING, CompanyStatus.ACTIVE): ProfileStatus.PENDING
    }
    
    return status_mapping.get((account_status, company_status))