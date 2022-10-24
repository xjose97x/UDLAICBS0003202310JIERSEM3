from utils import query_utils

def load(staging_db_context, core_db_context, etl_process_id):
    sales = query_utils.read_sql_by_process(table_name='SALES_TRA', columns=['PROD_ID', 'CUST_ID', 'TIME_ID', 'CHANNEL_ID', 'PROMO_ID', 'QUANTITY_SOLD', 'AMOUNT_SOLD'], etl_process_id=etl_process_id, db_context=staging_db_context)
    
    products_key_pairs = query_utils.get_surrogate_key_and_natural_key_pairs(table_name='PRODUCTS', natural_key_col='PROD_ID', db_context=core_db_context)
    customers_key_pairs = query_utils.get_surrogate_key_and_natural_key_pairs(table_name='CUSTOMERS', natural_key_col='CUST_ID', db_context=core_db_context)
    times_key_pairs = query_utils.get_surrogate_key_and_natural_key_pairs(table_name='TIMES', natural_key_col='TIME_ID', db_context=core_db_context)
    channels_key_pairs = query_utils.get_surrogate_key_and_natural_key_pairs(table_name='CHANNELS', natural_key_col='CHANNEL_ID', db_context=core_db_context)
    promotions_key_pairs = query_utils.get_surrogate_key_and_natural_key_pairs(table_name='PROMOTIONS', natural_key_col='PROMO_ID', db_context=core_db_context)

    sales['PROD_ID'] = sales['PROD_ID'].apply(lambda x: products_key_pairs[x])
    sales['CUST_ID'] = sales['CUST_ID'].apply(lambda x: customers_key_pairs[x])
    sales['TIME_ID'] = sales['TIME_ID'].apply(lambda x: times_key_pairs[x])
    sales['CHANNEL_ID'] = sales['CHANNEL_ID'].apply(lambda x: channels_key_pairs[x])
    sales['PROMO_ID'] = sales['PROMO_ID'].apply(lambda x: promotions_key_pairs[x])

    sales.to_sql('SALES', core_db_context, if_exists='append', index=False)