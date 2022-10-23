import pandas
from config import DataProperties


def truncate(db_context):
    db_context.execute('TRUNCATE TABLE CHANNELS_EXT')


def run(db_context):
    channels = pandas.read_csv(f'{DataProperties.DATA_PATH}/channels.csv')
    channels.to_sql('CHANNELS_EXT', db_context, if_exists='append', index=False)
