import pandas

def transform(db_context, etl_process_id):
    products_extract = pandas.read_sql_table(table_name='PRODUCTS_EXT', con=db_context, columns=['PROD_ID', 'PROD_NAME', 'PROD_DESC', 'PROD_CATEGORY', 'PROD_CATEGORY_ID', 'PROD_CATEGORY_DESC', 'PROD_WEIGHT_CLASS', 'SUPPLIER_ID', 'PROD_STATUS', 'PROD_LIST_PRICE', 'PROD_MIN_PRICE'])

    if not products_extract.empty:
        products_extract['PROD_ID'] = products_extract['PROD_ID'].astype(int)
        products_extract['PROD_CATEGORY_ID'] = products_extract['PROD_CATEGORY_ID'].astype(int)
        products_extract['PROD_WEIGHT_CLASS'] = products_extract['PROD_WEIGHT_CLASS'].astype(int)
        products_extract['SUPPLIER_ID'] = products_extract['SUPPLIER_ID'].astype(int)
        products_extract['PROD_LIST_PRICE'] = products_extract['PROD_LIST_PRICE'].astype(float)
        products_extract['PROD_MIN_PRICE'] = products_extract['PROD_MIN_PRICE'].astype(float)
        products_extract['ETL_PROCESS_ID'] = etl_process_id
        products_extract.to_sql(name='PRODUCTS_TRA', con=db_context, if_exists='append', index=False)

 