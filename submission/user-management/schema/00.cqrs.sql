CREATE SCHEMA cqrs;


--
-- Name: activity_msg_type; Type: TYPE; Schema: cqrs; Owner: -
--

CREATE TYPE cqrs.activity_msg_type AS ENUM (
    'USER_ACTION',
    'APP_REQUEST',
    'SYSTEM_CALL'
);


--
-- Name: activitymsgtype; Type: TYPE; Schema: cqrs; Owner: -
--

CREATE TYPE cqrs.activitymsgtype AS ENUM (
    'USER_ACTION',
    'APP_REQUEST',
    'SYSTEM_CALL'
);


--
-- Name: command_action; Type: TYPE; Schema: cqrs; Owner: -
--

CREATE TYPE cqrs.command_action AS ENUM (
    'CREATE',
    'UPDATE',
    'REMOVE'
);


--
-- Name: command_state; Type: TYPE; Schema: cqrs; Owner: -
--

CREATE TYPE cqrs.command_state AS ENUM (
    'SUCCESS',
    'CREATED',
    'PENDING',
    'RUNNING',
    'ERROR',
    'RETRY_1',
    'RETRY_2',
    'RETRY_3',
    'FAILED',
    'CANCELED'
);


--
-- Name: command_status; Type: TYPE; Schema: cqrs; Owner: -
--

CREATE TYPE cqrs.command_status AS ENUM (
    'SUCCESS',
    'CREATED',
    'PENDING',
    'RUNNING',
    'ERROR',
    'RETRY_1',
    'RETRY_2',
    'RETRY_3',
    'FAILED',
    'CANCELED'
);


--
-- Name: commandaction; Type: TYPE; Schema: cqrs; Owner: -
--

CREATE TYPE cqrs.commandaction AS ENUM (
    'CREATE',
    'UPDATE',
    'REMOVE'
);


--
-- Name: commandstate; Type: TYPE; Schema: cqrs; Owner: -
--

CREATE TYPE cqrs.commandstate AS ENUM (
    'SUCCESS',
    'CREATED',
    'PENDING',
    'RUNNING',
    'ERROR',
    'RETRY_1',
    'RETRY_2',
    'RETRY_3',
    'FAILED',
    'CANCELED'
);


--
-- Name: cqrs_entity_type; Type: TYPE; Schema: cqrs; Owner: -
--

CREATE TYPE cqrs.cqrs_entity_type AS ENUM (
    'QUERY',
    'EVENT',
    'COMMAND',
    'RESPONSE',
    'MESSAGE',
    'CONTEXT',
    'EVT_HANDLER',
    'CMD_HANDLER',
    'RESOURCE'
);


--
-- Name: cqrs_transport_type; Type: TYPE; Schema: cqrs; Owner: -
--

CREATE TYPE cqrs.cqrs_transport_type AS ENUM (
    'SANIC',
    'REDIS',
    'RABBITMQ',
    'KAFKA'
);


--
-- Name: cqrsentitytype; Type: TYPE; Schema: cqrs; Owner: -
--

CREATE TYPE cqrs.cqrsentitytype AS ENUM (
    'QUERY',
    'EVENT',
    'COMMAND',
    'RESPONSE',
    'MESSAGE',
    'CONTEXT',
    'EVT_HANDLER',
    'CMD_HANDLER',
    'RESOURCE'
);


--
-- Name: activity_log_search(); Type: FUNCTION; Schema: cqrs; Owner: -
--

CREATE FUNCTION cqrs.activity_log_search() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
            BEGIN
                UPDATE cqrs."activity-log" SET _txt = to_tsvector(';' || concat_ws( ' ', NEW.logroot__resource, NEW.message, NEW.msglabel )) WHERE _id = NEW._id;
                RETURN NEW;
            END;
            $$;


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: activity-log; Type: TABLE; Schema: cqrs; Owner: -
--

CREATE TABLE cqrs."activity-log" (
    _id uuid NOT NULL,
    logroot__identifier uuid,
    logroot__resource character varying,
    logroot__namespace character varying,
    context uuid,
    domain character varying,
    src_cmd uuid,
    src_evt uuid,
    data json,
    _created timestamp without time zone,
    transact uuid,
    message character varying,
    msgtype cqrs.activity_msg_type,
    code integer,
    msglabel character varying(255),
    _txt tsvector
);


--
-- Name: command-pending; Type: TABLE; Schema: cqrs; Owner: -
--

CREATE TABLE cqrs."command-pending" (
    _cqrs character varying,
    _created timestamp with time zone,
    _id uuid NOT NULL,
    _kind cqrs.cqrs_entity_type,
    _updated timestamp with time zone,
    _vers integer,
    aggroot__identifier uuid,
    aggroot__namespace character varying,
    aggroot__resource character varying,
    cmd_action cqrs.command_action,
    context uuid NOT NULL,
    data json,
    domain character varying,
    selector__identifier uuid,
    selector__resource character varying,
    status cqrs.command_status,
    stream_id uuid,
    transact uuid
);


--
-- Name: command-store; Type: TABLE; Schema: cqrs; Owner: -
--

CREATE TABLE cqrs."command-store" (
    _cqrs character varying,
    _created timestamp with time zone,
    _id uuid NOT NULL,
    _kind cqrs.cqrs_entity_type,
    _vers integer,
    aggroot__identifier uuid,
    aggroot__namespace character varying,
    aggroot__resource character varying,
    context uuid NOT NULL,
    data json,
    domain character varying,
    selector__identifier uuid,
    selector__resource character varying,
    status cqrs.command_status,
    transact uuid
);


--
-- Name: context-store; Type: TABLE; Schema: cqrs; Owner: -
--

CREATE TABLE cqrs."context-store" (
    _id uuid NOT NULL,
    namespace character varying,
    request_id uuid,
    session character varying,
    "timestamp" timestamp with time zone,
    user_id uuid,
    version character varying,
    revision integer,
    source character varying(255),
    transport cqrs.cqrs_transport_type
);


--
-- Name: event-store; Type: TABLE; Schema: cqrs; Owner: -
--

CREATE TABLE cqrs."event-store" (
    _cqrs character varying,
    _created timestamp with time zone,
    _id uuid NOT NULL,
    _kind cqrs.cqrs_entity_type,
    _vers integer,
    aggroot__identifier uuid,
    aggroot__namespace character varying,
    aggroot__resource character varying,
    context uuid,
    data json,
    domain character varying,
    src_cmd uuid,
    src_evt uuid,
    target__identifier uuid,
    target__resource character varying,
    transact uuid
);


--
-- Name: activity-log activity-log_pkey; Type: CONSTRAINT; Schema: cqrs; Owner: -
--

ALTER TABLE ONLY cqrs."activity-log"
    ADD CONSTRAINT "activity-log_pkey" PRIMARY KEY (_id);


--
-- Name: command-pending command-pending_pkey; Type: CONSTRAINT; Schema: cqrs; Owner: -
--

ALTER TABLE ONLY cqrs."command-pending"
    ADD CONSTRAINT "command-pending_pkey" PRIMARY KEY (_id);


--
-- Name: command-store command-store_pkey; Type: CONSTRAINT; Schema: cqrs; Owner: -
--

ALTER TABLE ONLY cqrs."command-store"
    ADD CONSTRAINT "command-store_pkey" PRIMARY KEY (_id);


--
-- Name: context-store context-store_pkey; Type: CONSTRAINT; Schema: cqrs; Owner: -
--

ALTER TABLE ONLY cqrs."context-store"
    ADD CONSTRAINT "context-store_pkey" PRIMARY KEY (_id);


--
-- Name: event-store event-store_pkey; Type: CONSTRAINT; Schema: cqrs; Owner: -
--

ALTER TABLE ONLY cqrs."event-store"
    ADD CONSTRAINT "event-store_pkey" PRIMARY KEY (_id);


--
-- Name: activity-log activity-log_context_fkey; Type: FK CONSTRAINT; Schema: cqrs; Owner: -
--

ALTER TABLE ONLY cqrs."activity-log"
    ADD CONSTRAINT "activity-log_context_fkey" FOREIGN KEY (context) REFERENCES cqrs."context-store"(_id);


--
-- Name: command-store command-store_context_fkey; Type: FK CONSTRAINT; Schema: cqrs; Owner: -
--

ALTER TABLE ONLY cqrs."command-store"
    ADD CONSTRAINT "command-store_context_fkey" FOREIGN KEY (context) REFERENCES cqrs."context-store"(_id);


--
-- PostgreSQL database dump complete
--

