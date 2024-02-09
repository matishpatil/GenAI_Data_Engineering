CREATE TABLE  dm.dim_locations
(
    location_id integer,
    source_system_id integer,
    city character varying(100),
    state_province character varying(100),
    country character varying(50),
    postal_code character varying(10),
    PRIMARY KEY (location_id)
)