from utils import query_utils

def load(staging_db_context, core_db_context, etl_process_id):
    customers = query_utils.read_sql_by_process(table_name='CUSTOMERS_TRA', columns=['CUST_ID', 'CUST_FIRST_NAME', 'CUST_LAST_NAME', 'CUST_GENDER', 'CUST_YEAR_OF_BIRTH', 'CUST_MARITAL_STATUS', 'CUST_STREET_ADDRESS', 'CUST_POSTAL_CODE', 'CUST_CITY', 'CUST_STATE_PROVINCE', 'COUNTRY_ID', 'CUST_MAIN_PHONE_INTEGER', 'CUST_INCOME_LEVEL', 'CUST_CREDIT_LIMIT', 'CUST_EMAIL'], etl_process_id=etl_process_id, db_context=staging_db_context)
    key_pairs = query_utils.get_surrogate_key_and_natural_key_pairs(table_name='COUNTRIES', natural_key_col='COUNTRY_ID', db_context=core_db_context)

    customers['COUNTRY_ID'] = customers['COUNTRY_ID'].apply(lambda x: key_pairs[x])
    customers.to_sql('CUSTOMERS', core_db_context, if_exists='append', index=False)