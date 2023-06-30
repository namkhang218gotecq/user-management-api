CREATE SCHEMA "gotecq--khang--user-management";

CREATE TYPE  "gotecq--khang--user-management"."account_status_type_enum" AS ENUM ('ACTIVE', 'INACTIVE', 'EXPIRED', 'PENDING');


CREATE TABLE "gotecq--khang--user-management".account (
	_id uuid PRIMARY KEY,
	telecom__email character varying(255),
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
	  company_name character varying(50),
	  telecom__email character varying(50),
	  telecom__phone character varying(20),
	  description character varying(200),
	  address__postal character varying(50), 
	  address__state character varying(50),
	  address__country character varying(50),
	  tax_id character varying(50),
	  category_name character varying(20),
	  company_code varchar(50),
	  npi varchar(20),
	  _created timestamp without time zone,
	  _creator uuid,
	  _deleted timestamp without time zone,
	  _updated timestamp without time zone,
	  _updater uuid,
	  _etag varchar(1024)
);


CREATE TYPE profile_status_type_enum AS ENUM ('PENDING', 'COMPANY_DEACTIVATED', 'EXPIRED', 'ACTIVE','DEACTIVATED','INACTIVE');
CREATE TYPE profile_gender_type_enum AS ENUM ('MALE', 'FEMALE');
CREATE TABLE "gotecq--khang--user-management".profile (
	_id uuid PRIMARY KEY,
	account_id uuid, 
	company_id uuid,
	password character varying(255),
	status profile_status_type_enum,
	name__family character varying(50),
	name__given character varying(50),
	telecom__email character varying(50),
	telecom__phone character varying(20),
	address__postal character varying(20),
	address__state character varying(20),
	address__country character varying(20),
	address__line character varying(20),
	gender profile_gender_type_enum,
	birth_date DATE,
	name__suffix varchar(50),
	name__prefix varchar(50),
	name__middle varchar(50),
	avatar uuid,
	 _created timestamp without time zone,
	 _creator uuid,
	 _deleted timestamp without time zone,
	 _updated timestamp without time zone,
	 _updater uuid,
	 _etag varchar(1024),
	FOREIGN KEY (account_id) REFERENCES  "gotecq--khang--user-management".account(_id),
	FOREIGN KEY (company_id) REFERENCES  "gotecq--khang--user-management".company(_id)
);

CREATE TYPE role_company_kind_enum AS ENUM ('SYSTEM', 'ORGANIZATION', 'NETWORK');

CREATE TABLE "gotecq--khang--user-management"."system-role" (
	_id uuid PRIMARY KEY,
	name character varying(50),
	key character varying(50),
	description character varying(500),
	active BOOLEAN,
    official_role BOOLEAN,
	company_kind role_company_kind_enum,
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
	company_id uuid,
    role_id uuid,
	_created timestamp without time zone,
	_creator uuid,
	_deleted timestamp without time zone,
	_updated timestamp without time zone,
	_updater uuid,
	_etag varchar(1024),
	FOREIGN KEY (profile_id) REFERENCES "gotecq--khang--user-management".profile(_id),
	FOREIGN KEY (company_id) REFERENCES "gotecq--khang--user-management".company(_id),
	FOREIGN KEY (system_role_id) REFERENCES "gotecq--khang--user-management"."system-role"(_id)
);


CREATE TABLE "gotecq--khang--user-management".company_role (
	_id uuid PRIMARY KEY,
	company_id uuid,
	role_id uuid,
	_created timestamp without time zone,
	_creator uuid,
	_deleted timestamp without time zone,
	_updated timestamp without time zone,
	_updater uuid,
	_etag varchar(1024),
	FOREIGN KEY (company_id) REFERENCES "gotecq--khang--user-management".company(_id),
	FOREIGN KEY (role_id) REFERENCES "gotecq--khang--user-management"."system-role"(_id));

CREATE OR REPLACE VIEW "gotecq--khang--user-management"."view--user-info" AS
SELECT
  a._id AS account_id,
  p._id AS profile_id,
  a.username AS account_username,
  p.name__family,
  p.name__given,
  p.telecom__email,
  p.telecom__phone,
  p.address__postal,
  p.address__state,
  p.address__country,
  p.address__line,
  p.gender,
  p.name__suffix,
  p.name__prefix,
  p.name__middle
FROM
  "gotecq--khang--user-management".account a
  JOIN "gotecq--khang--user-management".profile p ON a._id = p.account_id
WHERE
  a._deleted IS NULL
  AND p._deleted IS NULL;



CREATE OR REPLACE VIEW "gotecq--khang--user-management"."view--company-info" AS
SELECT c._id AS company_id, company_name, p._id AS profile_id,
       p.name__family, p.name__given, p.telecom__email, p.name__prefix,p.name__suffix,
       s.name AS role_name, s.key AS role_key, s.description AS role_description,
       cp._created,
       cp._creator,
       cp._etag,
       cp._deleted,
       cp._updated,
       cp._updater
FROM "gotecq--khang--user-management".company c
JOIN "gotecq--khang--user-management"."company-profile" cp ON c._id = cp.company_id
JOIN "gotecq--khang--user-management".profile p ON cp.profile_id = p._id
LEFT JOIN "gotecq--khang--user-management"."system-role" s ON cp.role_id = s._id
WHERE c._deleted IS NULL
  AND cp._deleted IS NULL;




CREATE OR REPLACE VIEW "gotecq--khang--user-management"."activity-log" AS
SELECT
    _id,
    logroot__identifier,
    logroot__resource,
    logroot__namespace,
    domain,
    _created,
    message,
    msgtype,
    msglabel
FROM "cqrs"."activity-log"
WHERE logroot__namespace = 'gotecq.user-management';


CREATE OR REPLACE VIEW "gotecq--khang--user-management"."view--dashboard-info" AS
SELECT
    (SELECT COUNT(*) FROM "gotecq--khang--user-management".company WHERE _deleted IS NULL) AS total_companies,
    (SELECT COUNT(*) FROM "gotecq--khang--user-management".company WHERE status = 'ACTIVE' AND _deleted IS NULL) AS active_companies,
    (SELECT COUNT(*) FROM "gotecq--khang--user-management".profile WHERE _deleted IS NULL) AS total_profiles,
    (SELECT COUNT(*) FROM "gotecq--khang--user-management".profile WHERE status = 'ACTIVE' AND _deleted IS NULL) AS active_profiles;



CREATE OR REPLACE VIEW "gotecq--khang--user-management"."view--company-kind" AS
with temp as (
	  SELECT * FROM (VALUES ('#143C55', 'ORGANIZATION'), ('#5AA5D7', 'SYSTEM'), ('#376EA5', 'NETWORK')) AS t (bg_color, kind)
)
select
	c.kind AS type,
	temp.bg_color,
	COUNT(*) AS amount
from "gotecq--khang--user-management".company c
left join temp on temp.kind = cast(c.kind as varchar)
where c._deleted is null
group by c.kind, temp.bg_color;

CREATE OR REPLACE VIEW "gotecq--khang--user-management"."view--company-status" AS
WITH temp AS (
  SELECT * FROM (VALUES 
    ('SETUP', '#93258E'),
    ('ACTIVE', '#43A047'),
    ('REVIEW', '#D4B106'),
    ('INACTIVE', '#A89BE')
  ) AS t (status, bg_color)
)
SELECT
  c.status AS status,
  temp.bg_color,
  COUNT(*) AS amount
FROM
  "gotecq--khang--user-management".company c
LEFT JOIN temp ON temp.status = cast(c.status as varchar)
WHERE
  c._deleted IS NULL
GROUP BY
  c.status, temp.bg_color;

CREATE OR REPLACE VIEW "gotecq--khang--user-management"."view--profile-status" AS
WITH temp AS (
  SELECT * FROM (VALUES 
    ('PENDING', '#93258E'),
    ('DEACTIVATED', '#FF4D4F'),
    ('ACTIVE', '#43A047'),
    ('EXPIRED', '#EE8D00'),
    ('INACTIVE', '#7F7F7F'),
    ('COMPANY_DEACTIVATED', '#93258E')
  ) AS t (status, bg_color)
)
SELECT
  c.status AS status,
  temp.bg_color,
  COUNT(*) AS amount
FROM
  "gotecq--khang--user-management".profile c
LEFT JOIN temp ON temp.status = cast(c.status as varchar)
WHERE
  c._deleted IS NULL
GROUP BY
  c.status, temp.bg_color;



CREATE OR REPLACE VIEW "gotecq--khang--user-management"."view--official-role" AS
SELECT
    p._id AS profile_id,
    p.name__family,
    p.name__given,
    p.telecom__email,
    p.telecom__phone,
    cp._id AS company_id,
    c.company_name,
    r.name AS role_name
FROM
    "gotecq--khang--user-management".profile p
JOIN
    "gotecq--khang--user-management"."company-profile" cp ON p._id = cp.profile_id
JOIN
    "gotecq--khang--user-management"."system-role" r ON cp.role_id = r._id
JOIN
    "gotecq--khang--user-management".company c ON cp.company_id = c._id
WHERE
    r.official_role = TRUE
    AND p._deleted IS NULL
    AND c._deleted IS NULL
    AND cp._deleted IS NULL;

