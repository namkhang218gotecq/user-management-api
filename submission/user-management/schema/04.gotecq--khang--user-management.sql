
CREATE SCHEMA "gotecq--khang--user-management";

CREATE TYPE account_status_type_enum AS ENUM ('ACTIVE', 'INACTIVE', 'EXPIRE', 'PENDING');

CREATE TABLE "gotecq--khang--user-management".account (
	_id uuid PRIMARY KEY,
	username character varying(255),
	password character varying(255),
	identity_number character varying(6),
	phone character varying(255),
	status account_status_type_enum,
	 _created timestamp without time zone,
	 _creator uuid,
	 _deleted timestamp without time zone,
	 _updated timestamp without time zone,
	 _updater uuid,
	 _etag varchar(1024)
);

CREATE TYPE company_status_type_enum AS ENUM ('SETUP', 'REVIEW', 'INACTIVE','ACTIVE');
CREATE TYPE company_kind_type_enum AS ENUM ('SYSTEM', 'ORGANIZATION', 'NETWORK');

CREATE TABLE "gotecq--khang--user-management".company (
	  _id uuid PRIMARY KEY,
	  status company_status_type_enum,
	  kind company_kind_type_enum,
	  name character varying(50),
	  email character varying(50),
	  phone character varying(20),
	  description character varying(200),
	  address__postal character varying(20), 
	  address__state character varying(20),
	  address__country character varying(20),
	  tax_id character varying(20),
	  category_name character varying(20),
	  _created timestamp without time zone,
	  _creator uuid,
	  _deleted timestamp without time zone,
	  _updated timestamp without time zone,
	  _updater uuid,
	  _etag varchar(1024)
);


CREATE TYPE profile_status_type_enum AS ENUM ('PENDING', 'COMPANY_DEACTIVATED', 'EXPIRED', 'ACTIVE','DEACTIVATED','INACTIVE');

CREATE TABLE "gotecq--khang--user-management".profile (
	_id uuid PRIMARY KEY,
	account_id uuid, 
	company_id uuid,
	password character varying(255),
	status profile_status_type_enum,
	first_name character varying(50),
	last_name character varying(50),
	telecom__email character varying(50),
	telecom__phone character varying(20),
	address__postal character varying(20),
	address__state character varying(20),
	address__country character varying(20),
	address__line character varying(20),
	 _created timestamp without time zone,
	 _creator uuid,
	 _deleted timestamp without time zone,
	 _updated timestamp without time zone,
	 _updater uuid,
	 _etag varchar(1024),
	FOREIGN KEY (account_id) REFERENCES  "gotecq--khang--user-management".account(_id),
	FOREIGN KEY (company_id) REFERENCES  "gotecq--khang--user-management".company(_id)
);

CREATE TABLE "gotecq--khang--user-management".role (
	_id uuid PRIMARY KEY,
	name character varying(50),
	key character varying(50),
	description character varying(200),
	active BOOLEAN,
	_created timestamp without time zone,
	_creator uuid,
	_deleted timestamp without time zone,
	_updated timestamp without time zone,
	_updater uuid,
	_etag varchar(1024)
);

CREATE TABLE "gotecq--khang--user-management"."company-profile" (
	_id uuid PRIMARY KEY,
	profile_id uuid,
	role_id uuid,
	company_id uuid,
	_created timestamp without time zone,
	_creator uuid,
	_deleted timestamp without time zone,
	_updated timestamp without time zone,
	_updater uuid,
	_etag varchar(1024),
	FOREIGN KEY (profile_id) REFERENCES "gotecq--khang--user-management".profile(_id),
	FOREIGN KEY (role_id) REFERENCES "gotecq--khang--user-management".role(_id),
	FOREIGN KEY (company_id) REFERENCES "gotecq--khang--user-management".company(_id)
);

