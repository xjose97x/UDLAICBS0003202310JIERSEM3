import pandas
from config import DataProperties

def truncate(db_context):
    db_context.execute('TRUNCATE TABLE TIMES')

def run(db_context):
    times = pandas.read_csv(f'{DataProperties.DATA_PATH}/times.csv', dtype="string")
    times = times.rename(columns={'DAY_NUMBER_IN_WEEK': 'DAY_INTEGER_IN_WEEK',
                    'DAY_NUMBER_IN_MONTH': 'DAY_INTEGER_IN_MONTH',
                    'CALENDAR_WEEK_NUMBER': 'CALENDAR_WEEK_INTEGER',
                    'CALENDAR_MONTH_NUMBER': 'CALENDAR_MONTH_INTEGER'})
    
    times['CALENDAR_MONTH_NAME'] = '' # Set empty value
    times.to_sql('TIMES_EXT', db_context, if_exists='append', index=False)
