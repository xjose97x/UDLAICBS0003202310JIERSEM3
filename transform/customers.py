import pandas

def transform(db_context, etl_process_id):
    customers_extract = pandas.read_sql_table(table_name='CUSTOMERS_EXT', con=db_context, columns=['CUST_ID', 'CUST_FIRST_NAME', 'CUST_LAST_NAME', 'CUST_GENDER', 'CUST_YEAR_OF_BIRTH', 'CUST_MARITAL_STATUS', 'CUST_STREET_ADDRESS', 'CUST_POSTAL_CODE', 'CUST_CITY', 'CUST_STATE_PROVINCE', 'COUNTRY_ID', 'CUST_MAIN_PHONE_INTEGER', 'CUST_INCOME_LEVEL', 'CUST_CREDIT_LIMIT', 'CUST_EMAIL' ])

    if not customers_extract.empty:
        customers_extract['CUST_ID'] = customers_extract['CUST_ID'].astype(int)
        customers_extract['COUNTRY_ID'] = customers_extract['COUNTRY_ID'].astype(int)
        customers_extract['CUST_CREDIT_LIMIT'] = customers_extract['CUST_CREDIT_LIMIT'].astype(int)
        customers_extract['ETL_PROCESS_ID'] = etl_process_id
        customers_extract.to_sql(name='CUSTOMERS_TRA', con=db_context, if_exists='append', index=False)