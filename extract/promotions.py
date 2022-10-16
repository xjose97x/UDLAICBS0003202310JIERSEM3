import pandas
from config import DataProperties

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE PROMOTIONS')

def run(db_context):
    promotions = pandas.read_csv(f'{DataProperties.DATA_PATH}/promotions.csv')
    promotions.to_sql('PROMOTIONS', db_context, if_exists='append', index=False)