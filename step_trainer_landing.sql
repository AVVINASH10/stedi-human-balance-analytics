create external table IF not exists stedi.step_trainer_landing (
    sensorreadingtime bigint,
    serialnumber string,
    distancefromobject int
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://stedi-human-balance-avvinash/step_trainer/landing/'
tblproperties ('has_encrypted_data'='false');