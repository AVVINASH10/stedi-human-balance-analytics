import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

step_trainer = spark.read.json(
    "s3://stedi-human-balance-avvinash/step_trainer/landing/"
)

customer_curated = spark.read.json(
    "s3://stedi-human-balance-avvinash/customer/curated/"
)

trusted = step_trainer.join(
    customer_curated,
    step_trainer["serialNumber"] == customer_curated["serialnumber"]
).select(step_trainer["*"]).distinct()

trusted.write.mode("overwrite").json(
    "s3://stedi-human-balance-avvinash/step_trainer/trusted/"
)

job.commit()