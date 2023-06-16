

def combine_profile_status(account_status: str, company_status: str) -> str:
    from fii import logger
    logger.warning("Account status --> %s", account_status)
    logger.warning("Company status --> %s", company_status)
    status_mapping = {
        ("ACTIVE", "SETUP"): "ACTIVE",
        ("ACTIVE", "REVIEW"): "ACTIVE",
        ("ACTIVE", "INACTIVE"): "COMPANY_DEACTIVATED",
        ("ACTIVE", "ACTIVE"): "ACTIVE",
        
        ("INACTIVE", "SETUP"): "INACTIVE",
        ("INACTIVE", "REVIEW"): "INACTIVE",
        ("INACTIVE", "INACTIVE"): "DEACTIVATED",
        ("INACTIVE", "ACTIVE"): "DEACTIVATED",
        
        ("EXPIRED", "SETUP"): "EXPIRED",
        ("EXPIRED", "REVIEW"): "EXPIRED",
        ("EXPIRED", "INACTIVE"): "EXPIRED",
        ("EXPIRED", "ACTIVE"): "EXPIRED",
        
        ("PENDING", "SETUP"): "PENDING",
        ("PENDING", "REVIEW"): "PENDING",
        ("PENDING", "INACTIVE"): "COMPANY_DEACTIVATED",
        ("PENDING", "ACTIVE"): "PENDING"
    }
    
    return status_mapping.get((account_status, company_status), "UNKNOWN")