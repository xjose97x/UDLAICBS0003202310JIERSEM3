import pandas
from utils.db_connection import Db_Connection
from config import StagingProperties, DataProperties

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE CHANNELS')

def run(db_context):
    channels = pandas.read_csv(f'{DataProperties.DATA_PATH}/channels.csv')
    channels.to_sql('CHANNELS', db_context, if_exists='append', index=False)
