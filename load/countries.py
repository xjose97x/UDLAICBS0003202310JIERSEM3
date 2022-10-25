from utils import query_utils

def load(staging_db_context, core_db_context, etl_process_id):
    countries = query_utils.read_sql_by_process(table_name='COUNTRIES_TRA', columns=['COUNTRY_ID', 'COUNTRY_NAME', 'COUNTRY_REGION', 'COUNTRY_REGION_ID'], etl_process_id=etl_process_id, db_context=staging_db_context)
    query_utils.upsert(table_name='COUNTRIES', natural_key_cols=['COUNTRY_ID'], dataframe= countries, db_context=core_db_context)
