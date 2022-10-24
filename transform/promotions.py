import pandas
from .transformations import datetime_from_str

def transform(db_context, etl_process_id):
    promotions_extract = pandas.read_sql_table(table_name='PROMOTIONS_EXT', con=db_context, columns=['PROMO_ID', 'PROMO_NAME', 'PROMO_COST', 'PROMO_BEGIN_DATE', 'PROMO_END_DATE'])

    if not promotions_extract.empty:
        promotions_extract['PROMO_ID'] = promotions_extract['PROMO_ID'].astype(int)
        promotions_extract['PROMO_COST'] = promotions_extract['PROMO_COST'].astype(float)
        promotions_extract['PROMO_BEGIN_DATE'] = promotions_extract['PROMO_BEGIN_DATE'].apply(lambda x: datetime_from_str(x))
        promotions_extract['PROMO_END_DATE'] = promotions_extract['PROMO_END_DATE'].apply(lambda x: datetime_from_str(x))
        promotions_extract['ETL_PROCESS_ID'] = etl_process_id
        promotions_extract.to_sql(name='PROMOTIONS_TRA', con=db_context, if_exists='append', index=False)