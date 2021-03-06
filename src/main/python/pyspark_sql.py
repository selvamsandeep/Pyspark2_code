from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, FloatType
from pyspark.sql.functions import *

spark = SparkSession. \
    builder. \
    master('local'). \
    appName('getting started'). \
    getOrCreate()

orders_csv = spark. \
    read.csv("/media/selva/d/Big data/data/retail_db/orders"). \
    toDF('order_id', 'order_date', 'order_customer_id', 'order_status')

orders = orders_csv. \
    withColumn('order_id', orders_csv.order_id.cast(IntegerType())). \
    withColumn('order_customer_id', orders_csv.order_customer_id.cast(IntegerType()))

orders.printSchema()
#orders.show()

order_items_csv = spark. \
    read.csv('/media/selva/d/Big data/data/retail_db/order_items'). \
    toDF('order_item_id', 'order_item_order_id', 'order_item_product_id',
         'order_item_quantity', 'order_item_subtotal', 'order_item_product_price')

order_items = order_items_csv. \
    withColumn('order_item_id', order_items_csv.order_item_id.cast(IntegerType())). \
    withColumn('order_item_order_id', order_items_csv.order_item_order_id.cast(IntegerType())). \
    withColumn('order_item_product_id', order_items_csv.order_item_product_id.cast(IntegerType())). \
    withColumn('order_item_quantity', order_items_csv.order_item_quantity.cast(IntegerType())). \
    withColumn('order_item_subtotal', order_items_csv.order_item_subtotal.cast(FloatType())). \
    withColumn('order_item_product_price', order_items_csv.order_item_product_price.cast(FloatType()))

order_items.printSchema()

car_orders = spark.read. \
    format('jdbc'). \
    option('url', 'jdbc:mysql://127.0.0.1:3306'). \
    option('dbtable', 'classicmodels.orders'). \
    option('user', 'root'). \
    option('password', 'suntv'). \
    load()

car_orders.printSchema()
car_orders.show()

orders.select(substring('order_date', 1, 7)).show()
orders.withColumn('order_status', lower(orders.order_status)).show()
orders.withColumn('order_Year_month', date_format('order_date', 'YYYYMM')).show()
