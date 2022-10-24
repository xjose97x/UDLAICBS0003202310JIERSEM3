from utils import query_utils

def load(staging_db_context, core_db_context, etl_process_id):
    times = query_utils.read_sql_by_process(table_name='TIMES_TRA', columns=['TIME_ID', 'DAY_NAME', 'DAY_INTEGER_IN_WEEK', 'DAY_INTEGER_IN_MONTH', 'CALENDAR_WEEK_INTEGER', 'CALENDAR_MONTH_INTEGER', 'CALENDAR_MONTH_DESC', 'END_OF_CAL_MONTH', 'CALENDAR_MONTH_NAME', 'CALENDAR_QUARTER_DESC', 'CALENDAR_YEAR'], etl_process_id=etl_process_id, db_context=staging_db_context)
    times.to_sql('TIMES', core_db_context, if_exists='append', index=False)