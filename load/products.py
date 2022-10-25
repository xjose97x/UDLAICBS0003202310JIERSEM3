from utils import query_utils

def load(staging_db_context, core_db_context, etl_process_id):
    products = query_utils.read_sql_by_process(table_name='PRODUCTS_TRA', columns=['PROD_ID', 'PROD_NAME', 'PROD_DESC', 'PROD_CATEGORY', 'PROD_CATEGORY_ID', 'PROD_CATEGORY_DESC', 'PROD_WEIGHT_CLASS', 'SUPPLIER_ID', 'PROD_STATUS', 'PROD_LIST_PRICE', 'PROD_MIN_PRICE'], etl_process_id=etl_process_id, db_context=staging_db_context)
    query_utils.upsert(table_name='PRODUCTS', natural_key_cols=['PROD_ID'], dataframe= products, db_context=core_db_context)