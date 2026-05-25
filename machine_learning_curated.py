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
    "s3://stedi-human-balance-avvinash/step_trainer/trusted/"
)

accelerometer = spark.read.json(
    "s3://stedi-human-balance-avvinash/accelerometer/landing/"
)

ml_curated = step_trainer.join(
    accelerometer,
    step_trainer["sensorReadingTime"] == accelerometer["timestamp"]
).distinct()

ml_curated.write.mode("overwrite").json(
    "s3://stedi-human-balance-avvinash/machine_learning/curated/"
)

job.commit()