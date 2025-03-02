from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col, when

# Initialize Spark session
spark = SparkSession.builder.appName("MarketingCampaign").getOrCreate()

# Load the CSV file into a Spark DataFrame
df = spark.read.csv("marketing_campaign_data.csv", header=True, inferSchema=True)

# Aggregate total units sold per product
product_sales = df.groupBy("product_id").agg(sum("quantity").alias("total_units_sold"))

# Define ad performance classification using `when` and `otherwise`
product_sales = product_sales.withColumn(
    "ad_performance",
    when(col("total_units_sold") >= 30, "Outstanding")
    .when((col("total_units_sold") >= 20) & (col("total_units_sold") <= 29), "Satisfactory")
    .when((col("total_units_sold") >= 10) & (col("total_units_sold") <= 19), "Unsatisfactory")
    .when((col("total_units_sold") >= 1) & (col("total_units_sold") <= 9), "Poor")
    .otherwise("No Sales")
)

# Sort the results by total units sold in descending order
product_sales = product_sales.orderBy(col("total_units_sold").desc())

# Show the result
product_sales.show()
