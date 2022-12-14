import pandas
from config import DataProperties

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE COUNTRIES')

def run(db_context):
    countries = pandas.read_csv(f'{DataProperties.DATA_PATH}/countries.csv')
    countries.to_sql('COUNTRIES', db_context, if_exists='append', index=False)