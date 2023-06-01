CREATE SCHEMA "gotecq--internship";

CREATE TABLE "gotecq--internship".boilerplate (
    _id uuid PRIMARY KEY,
    _created timestamp without time zone,
    _updated timestamp without time zone,
    _deleted timestamp without time zone,
    _etag character varying(255),
    _creator uuid,
    _updater uuid,
    name character varying(255),
    description character varying
);

CREATE TABLE "gotecq--internship".card (
    _id uuid PRIMARY KEY,
    password varchar(600),
    balance_inquiry float(8),
    client_id uuid,
    _created timestamp without time zone,
    _creator uuid,
    _deleted timestamp without time zone,
    _etag character varying(255),
    _updated timestamp without time zone,
    _updater uuid,
);

