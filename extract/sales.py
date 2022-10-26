import pandas
from config import DataProperties

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE SALES_EXT')

def run(db_context):
    channels = pandas.read_csv(f'{DataProperties.DATA_PATH}/sales.csv')
    channels.to_sql('SALES_EXT', db_context, if_exists='append', index=False)
