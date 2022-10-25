from utils import query_utils

def load(staging_db_context, core_db_context, etl_process_id):
    promotions = query_utils.read_sql_by_process(table_name='PROMOTIONS_TRA', columns=['PROMO_ID', 'PROMO_NAME', 'PROMO_COST', 'PROMO_BEGIN_DATE', 'PROMO_END_DATE'], etl_process_id=etl_process_id, db_context=staging_db_context)
    query_utils.upsert(table_name='PROMOTIONS', natural_key_cols=['PROMO_ID'], dataframe= promotions, db_context=core_db_context)
