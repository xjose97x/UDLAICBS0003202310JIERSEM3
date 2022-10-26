import pandas
from config import DataProperties

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE CUSTOMERS_EXT')

def run(db_context):
    customers = pandas.read_csv(f'{DataProperties.DATA_PATH}/customers.csv')
    customers = customers.rename(columns={'CUST_MAIN_PHONE_NUMBER': 'CUST_MAIN_PHONE_INTEGER'})
    customers.to_sql('CUSTOMERS_EXT', db_context, if_exists='append', index=False)