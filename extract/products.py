import pandas
from utils.db_connection import Db_Connection
from config import StagingProperties, DataProperties

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE PRODUCTS')

def run(db_context):
    products = pandas.read_csv(f'{DataProperties.DATA_PATH}/products.csv')
    products.to_sql('PRODUCTS', db_context, if_exists='append', index=False)
    db_context.dispose()