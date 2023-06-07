# User Management Data Model Feedback

## Relation
- Relation between company and profile must be one-many. One company can have many profiles and one profile must link to only one specific company.

## Data

### Table `role`
- In application we have 2 role kinds:
    - SYSTEM - Define by system
    - USER - Define by user
--> You can define one field in table role to specify each role kind, or create 2 table `system-role` and `user-role` and create one view using `UNION`

- Each role in table `role` must have one field to define this role belong to one `company_kind`: `SYSTEM`, `NETWORK`, `ORGANIZATION`

### Table `company`
- Add more information about the company, ex:
    - NPI
    - company_code: for SYSTEM and NETWORK company
### Table `profile`
- Add more information about the profile, ex:
    - gender
    - birth_date
    - avatar : using s3media in fii_s3media to upload images
    - detail name: name__suffix, name__prefix, name__middle

## Naming convention
- In table  `company` using `telecom__email` and `telecom__phone` fields
- In table `profile` replace `first_name` and `last_name` with `name__family` and `name__given` fields 

## Limit characters in character data type
- Number of characters should in 2^x form, ex: 256,1024
- Except you known exactly number of characters of data like member_identifier must be in 11 characters