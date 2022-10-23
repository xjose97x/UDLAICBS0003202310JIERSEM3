import pandas
from config import DataProperties

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE COUNTRIES_EXT')

def run(db_context):
    countries = pandas.read_csv(f'{DataProperties.DATA_PATH}/countries.csv')
    countries.to_sql('COUNTRIES_EXT', db_context, if_exists='append', index=False)