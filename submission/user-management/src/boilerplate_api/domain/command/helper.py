

def combine_profile_status(account_status: str, company_status: str) -> str:
    status_mapping = {
        ("SETUP", "SETUP"): "SETUP",
        ("SETUP", "REVIEW"): "SETUP",
        ("REVIEW", "SETUP"): "SETUP",
        ("REVIEW", "REVIEW"): "REVIEW",
        ("PENDING", "ACTIVE"): "PENDING",
        ("PENDING", "INACTIVE"): "COMPANY_DEACTIVATED",
        ("EXPIRED", "ACTIVE"): "EXPIRED",
        ("EXPIRED", "INACTIVE"): "EXPIRED",
        ("ACTIVE", "ACTIVE"): "ACTIVE",
        ("ACTIVE", "INACTIVE"): "COMPANY_DEACTIVATED",
        ("INACTIVE", "ACTIVE"): "DEACTIVATED",
        ("INACTIVE", "INACTIVE"): "DEACTIVATED",
    }
    
    return status_mapping.get((account_status, company_status), "UNKNOWN")