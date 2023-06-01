## QUERY

### Query for dashboard

#### Data respone:

```bash
{
		"total__companies": 694,
		"active__companies" 54,
		"total_profiles": 1790,
		"active__profiles":1083
}
```

### User Statistics/Company Statistics

#### Data respone:

```bash
{
	"status": "SETUP",
	"amount": "423",
	"bg_color": "#8E8E8E",
}
```

### User info + other profiles

#### Data respone:

```bash
 {
		"_id": "7d3d4e3b-21c0-4d25-b530-85f9be84e6f1"
		"first__name": "baby",
		"last__name" "five",
		"prefix": "Dr.",
		"suffix":"D.D.S",
		"telecom__email": "demo+user36@gotecq.com",
		"telecom__fax": null,
		"telecom__phone": null,
		"username": "demo+user36@gotecq.com",
		"status": "ACTIVE",
		"account_id": "",
		"company_id": ""
}
```

### Company info (advance: show users + roles in these company)

#### Data respone:

```bash
{
		"_id": "5d943edb-bacf-44db-bad9-6342e848b12d",
		"kind": "ORGANIZATION",
		"description": null,
		"status": "SETUP",
		"name": "A PLUS DENTAL ASSOCIATES PLLC",
		"members": [<"list id profile belong to company">]
}
```

### Show user have official role in company

#### Data respone:

```bash
{
		"company_id":"107d76b4-7b0d-401b-8dd5-0c84b8da04f7"
		"description": "On the Provider Portal, this role allows users to view patients of the organization, perform functions such as editing contracts, updating patient information, adding patient surveys, allocating and delivering items..."
		"profile_status": "active",
		"status": "Active",
		"role_name": "Organization Contract Editor",
		"username": "Henry Tran",
		"telecom__email": "demo+user36@gotecq.com"

}
```

### Log activity

#### Data respone:

```bash
{
		"user_id":"107d76b4-7b0d-401b-8dd5-0c84b8da04f7"
		"content": "Your data has been exported successfully. Please check the attachment section below for detail."
		"content_type": "MARKDOWN",
		"direction": "INCOMING",
		"subject": "Exported file is ready. [STAGING]",
		"username": "Henry Tran"
}
```
