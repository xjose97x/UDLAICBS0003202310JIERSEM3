import pandas
from .transformations import datetime_from_str

def transform(db_context, etl_process_id):
    times_extract = pandas.read_sql_table(table_name='TIMES_EXT', con=db_context, columns=['TIME_ID', 'DAY_NAME', 'DAY_INTEGER_IN_WEEK', 'DAY_INTEGER_IN_MONTH', 'CALENDAR_WEEK_INTEGER', 'CALENDAR_MONTH_INTEGER', 'CALENDAR_MONTH_DESC', 'END_OF_CAL_MONTH', 'CALENDAR_MONTH_NAME', 'CALENDAR_QUARTER_DESC', 'CALENDAR_YEAR'])

    if not times_extract.empty:
        times_extract['TIME_ID'] = times_extract['TIME_ID'].apply(lambda x: datetime_from_str(x))
        times_extract['DAY_INTEGER_IN_WEEK'] = times_extract['DAY_INTEGER_IN_WEEK'].astype(int)
        times_extract['DAY_INTEGER_IN_MONTH'] = times_extract['DAY_INTEGER_IN_MONTH'].astype(int)
        times_extract['CALENDAR_WEEK_INTEGER'] = times_extract['CALENDAR_WEEK_INTEGER'].astype(int)
        times_extract['CALENDAR_MONTH_INTEGER'] = times_extract['CALENDAR_MONTH_INTEGER'].astype(int)
        times_extract['END_OF_CAL_MONTH'] = times_extract['END_OF_CAL_MONTH'].apply(lambda x: datetime_from_str(x))
        times_extract['CALENDAR_YEAR'] = times_extract['CALENDAR_YEAR'].astype(int)
        times_extract['ETL_PROCESS_ID'] = etl_process_id
        times_extract.to_sql(name='TIMES_TRA', con=db_context, if_exists='append', index=False)