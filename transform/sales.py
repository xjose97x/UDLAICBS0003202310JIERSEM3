import pandas
from .transformations import datetime_from_str

def transform(db_context, etl_process_id):
    sales_extract = pandas.read_sql_table(table_name='SALES_EXT', con=db_context, columns=['PROD_ID', 'CUST_ID', 'TIME_ID', 'CHANNEL_ID', 'PROMO_ID', 'QUANTITY_SOLD', 'AMOUNT_SOLD'])

    if not sales_extract.empty:
        sales_extract['PROD_ID'] = sales_extract['PROD_ID'].astype(int)
        sales_extract['CUST_ID'] = sales_extract['CUST_ID'].astype(int)
        sales_extract['TIME_ID'] = sales_extract['TIME_ID'].apply(lambda x: datetime_from_str(x))
        sales_extract['CHANNEL_ID'] = sales_extract['CHANNEL_ID'].astype(int)
        sales_extract['PROMO_ID'] = sales_extract['PROMO_ID'].astype(int)
        sales_extract['QUANTITY_SOLD'] = sales_extract['QUANTITY_SOLD'].astype(float)
        sales_extract['AMOUNT_SOLD'] = sales_extract['AMOUNT_SOLD'].astype(float)
        sales_extract['ETL_PROCESS_ID'] = etl_process_id
        sales_extract.to_sql(name='SALES_TRA', con=db_context, if_exists='append', index=False)
