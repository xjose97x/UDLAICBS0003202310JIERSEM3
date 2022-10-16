import pandas
from utils.db_connection import Db_Connection
from config import StagingProperties, DataProperties

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE CUSTOMERS')

def run(db_context):
    customers = pandas.read_csv(f'{DataProperties.DATA_PATH}/customers.csv')
    customers = customers.rename(columns={'CUST_MAIN_PHONE_NUMBER': 'CUST_MAIN_PHONE_INTEGER'})
    customers.to_sql('CUSTOMERS', db_context, if_exists='append', index=False)