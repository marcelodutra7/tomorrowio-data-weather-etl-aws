# importando bibliotecas
import sys
import boto3
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, year, month, dayofmonth

# Obtém os argumentos do job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Parâmetros de entrada e saída
data_source = "raw_db"
output_path = 's3://weather-data-tomorrowio-rt/gold/'

# Inicializa o cliente boto3 para Glue
glue_client = boto3.client('glue')

# Obtém a lista de tabelas no banco de dados Glue
tables = glue_client.get_tables(DatabaseName=data_source)['TableList']

for table in tables:
    table_name = table['Name']
    
    # Lê os dados JSON do catálogo do Glue
    datasource = glueContext.create_dynamic_frame.from_catalog(
        database=data_source,
        table_name=table_name,
        transformation_ctx="datasource"
    )

    # Converte DynamicFrame para DataFrame para manipulação com Spark
    df = datasource.toDF()

    # Seleciona e renomeia os campos relevantes
    flattened_df = df.select(
        col("data.time").alias("time"),
        col("data.values.cloudBase").alias("cloudBase"),
        col("data.values.cloudCeiling").alias("cloudCeiling"),
        col("data.values.cloudCover").alias("cloudCover"),
        col("data.values.dewPoint").alias("dewPoint"),
        col("data.values.freezingRainIntensity").alias("freezingRainIntensity"),
        col("data.values.humidity").alias("humidity"),
        col("data.values.precipitationProbability").alias("precipitationProbability"),
        col("data.values.pressureSurfaceLevel").alias("pressureSurfaceLevel"),
        col("data.values.rainIntensity").alias("rainIntensity"),
        col("data.values.sleetIntensity").alias("sleetIntensity"),
        col("data.values.snowIntensity").alias("snowIntensity"),
        col("data.values.temperature").alias("temperature"),
        col("data.values.temperatureApparent").alias("temperatureApparent"),
        col("data.values.uvHealthConcern").alias("uvHealthConcern"),
        col("data.values.uvIndex").alias("uvIndex"),
        col("data.values.visibility").alias("visibility"),
        col("data.values.weatherCode").alias("weatherCode"),
        col("data.values.windDirection").alias("windDirection"),
        col("data.values.windGust").alias("windGust"),
        col("data.values.windSpeed").alias("windSpeed"),
        col("location.lat").alias("latitude"),
        col("location.lon").alias("longitude")
    )

    # Extrai ano, mês e dia da coluna de tempo para particionamento
    flattened_df = flattened_df.withColumn('year', year(flattened_df['time']))
    flattened_df = flattened_df.withColumn('month', month(flattened_df['time']))
    flattened_df = flattened_df.withColumn('day', dayofmonth(flattened_df['time']))

    # Converte de volta para DynamicFrame para escrita no Glue
    dynamic_frame = DynamicFrame.fromDF(flattened_df, glueContext, "dynamic_frame")

    # Grava os dados no formato Parquet, particionado por ano, mês e dia
    glueContext.write_dynamic_frame.from_options(
        frame=dynamic_frame,
        connection_type="s3",
        connection_options={
            "path": output_path,
            "partitionKeys": ["year", "month", "day"]
        },
        format="parquet"
    )

# Finaliza o job do Glue
job.commit()