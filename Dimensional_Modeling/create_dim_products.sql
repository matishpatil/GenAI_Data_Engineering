CREATE TABLE dm.dim_products
(
    product_id integer,
    source_system_id integer,
    product_name character varying(100),
    product_category character varying(50),,
    PRIMARY KEY (product_id)
)