## COMMAND

### Create user

##### http://api.local.gotecq.net/gotecq.user-management:create-user/account POST

body:

```bash
{
  "email”: “john.thomas@gmail.com",
  "username”: “johnthomas",
  "password”: “password123",
  "identity_number”: “123456",
  "status": "ACTIVE"
}
```

### Update user

##### http://api.local.gotecq.net/gotecq.user-management:update-user/account/{id} PUT

##### params: \_id

##### body:

```bash
{
  "first_name”: “baby",
  "last_name": "five",
  "prefix”: “Dr.",
  "suffix”: “D.D.S",
	"telecom__email": "demo+user36@gotecq.com",
	"telecom__fax": null,
	"telecom__phone": null,
}
```

### Add user to company role

##### http://api.local.gotecq.net/gotecq.user-management:add-user-role/company/{id} POST

##### params: \_id

##### body:

```bash
{
"key" :"",
"role_id": "",
"first_name": "baby",
"last_name": "five",
"prefix”: “Dr.",
"suffix”: “D.D.S",
"telecom__email": "demo+user36@gotecq.com"
}
```

### Suspend proflie

##### http://api.local.gotecq.net/gotecq.user-management:suspend-profile/proflie/{id} PUT

##### params: \_id

### Active profile

##### http://api.local.gotecq.net/gotecq.user-management:active-profile/proflie/{id} PUT

##### params: \_id

### Deactivate account:

##### http://api.local.gotecq.net/gotecq.user-management:deactivate-profile/proflie/{id} PUT

##### params: \_id

### Activate account

##### http://api.local.gotecq.net/gotecq.user-management:activate-profile/proflie/{id} PUT

##### params: \_id

### Create company

##### http://api.local.gotecq.net/gotecq.user-management:create-company/company POST

##### params: \_id

##### body:

```bash
{
	"name": "KHANG COMPANY",
	"company_status": "ACTIVE",
	"contact_entity": "ORGANIZATION",
	"category": "PROVIDER_ORGANIZATION",
	"category_name": "Provider Organization",
	"address__city": "Gold Hill",
	"address_country": "Houston",
	"tax_id":"123123123",
	"address__line": null,
	"address__postal": "",
	"address__state" : "",
	"telecom__email": "",
	"telecom__fax": "",
	"telecom__phone" : "0923557355",
	"primary_taxonomy_code": "332B00000X"
	"primary_taxonomy_common_name":"Durable Medical Equipment & Medical Supplies"
}
```

### Update company

##### http://api.local.gotecq.net/gotecq.user-management:create-company/company/{id} PUT

##### params: \_id

##### body:

```bash
{
	"name": "KHANG COMPANY",
	"category_name": "Provider Organization",
	"tax_id": "123123123",
	"primary_taxonomy_code": "332B00000X"
	"primary_taxonomy_common_name":"Durable Medical Equipment & Medical Supplies"

}
```

### Add company member

##### http://api.local.gotecq.net/gotecq.user-management:add-member/company/{id} POST

##### params: \_id

##### body:

```bash
{
"key" :"",
"role_id": "",
"role_name": "Organization Operator",
"first_name": "baby",
"last_name": "five",
"prefix”: “Dr.",
"suffix”: “D.D.S",
"telecom__email": "demo+user36@gotecq.com"
}
```

### Remove company member

##### http://api.local.gotecq.net/gotecq.user-management:delete-member/company/{id} DELETE

##### params: \_id

### Deactivate company

##### http://api.local.gotecq.net/gotecq.user-management:deactivate-company/company/{id} PUT

##### params: \_id

### Activate company

##### http://api.local.gotecq.net/gotecq.user-management:activate-member/company/{id} PUT

##### params: \_id
