CREATE EXTERNAL TABLE IF NOT EXISTS stedi.accelerometer_landing (
    timestamp BIGINT,
    user STRING,
    x DOUBLE,
    y DOUBLE,
    Z DOUBLE
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://stedi-human-balance-avvinash/accelerometer/landing/'
tblproperties ('has_encrypted_data'='false');