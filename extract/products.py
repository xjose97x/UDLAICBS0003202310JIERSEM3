import pandas
from config import DataProperties

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE PRODUCTS')

def run(db_context):
    products = pandas.read_csv(f'{DataProperties.DATA_PATH}/products.csv')
    products.to_sql('PRODUCTS_EXT', db_context, if_exists='append', index=False)