CREATE TABLE "gotecq--khang--atm".customer (
_id uuid PRIMARY KEY,
identity_number character varying(6),
fist_name character varying(255),
last_name character varying(255),
phone character varying(255),
address__city character varying(255),
 _created timestamp without time zone,
 _creator uuid,
 _deleted timestamp without time zone,
 _updated timestamp without time zone,
 _updater uuid,
 _etag varchar(1024)
);
CREATE TABLE "gotecq--khang--atm".card (
_id uuid PRIMARY KEY,
customer_id uuid, 
password character varying(255),
balance float,
 _created timestamp without time zone,
 _creator uuid,
 _deleted timestamp without time zone,
 _updated timestamp without time zone,
 _updater uuid,
 _etag varchar(1024),
FOREIGN KEY (customer_id) REFERENCES "gotecq--khang--atm".customer(_id)
);

CREATE TABLE "gotecq--khang--atm".transaction_record (
_id uuid PRIMARY KEY,
card_id uuid, 
receiver_card_id uuid, 
amount float,
message character varying(255),
_created timestamp without time zone,
 _creator uuid,
 _deleted timestamp without time zone,
 _updated timestamp without time zone,
 _updater uuid,
 _etag varchar(1024),
FOREIGN KEY (card_id) REFERENCES "gotecq--khang--atm".card(_id)
);

CREATE TYPE transaction_type_enum AS ENUM ('deposit', 'transfer', 'withdraw');

CREATE TABLE "gotecq--khang--atm".transaction_type (
  _id uuid PRIMARY KEY,
  transaction_type transaction_type_enum,
  description character varying(255),
_created timestamp without time zone,
 _creator uuid,
 _deleted timestamp without time zone,
 _updated timestamp without time zone,
 _updater uuid,
 _etag varchar(1024)
);

ALTER TABLE "gotecq--khang--atm".transaction_record
ADD COLUMN transaction_type_id uuid,
ADD CONSTRAINT fk_transaction_type
  FOREIGN KEY (transaction_type_id)
  REFERENCES "gotecq--khang--atm".transaction_type(_id);

ALTER TABLE "gotecq--khang--atm".transaction_record
DROP COLUMN receiver_card_id;

ALTER TABLE "gotecq--khang--atm".transaction_record
ADD COLUMN destination_card_id uuid,
ADD CONSTRAINT fk_destination_card
  FOREIGN KEY (destination_card_id)
  REFERENCES "gotecq--khang--atm".card(_id);

ALTER TABLE "gotecq--khang--atm".transaction_record
ADD COLUMN source_card_id uuid,
ADD CONSTRAINT fk_source_card
  FOREIGN KEY (source_card_id)
  REFERENCES "gotecq--khang--atm".card(_id);

ALTER TABLE "gotecq--khang--atm".transaction_record
ADD COLUMN amount float;

ALTER TABLE "gotecq--khang--atm".transaction_record
DROP COLUMN amount_transaction;

