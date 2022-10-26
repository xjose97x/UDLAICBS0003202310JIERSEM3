from itertools import count
import pandas

def transform(db_context, etl_process_id):
    countries_extract = pandas.read_sql_table(table_name='COUNTRIES_EXT', con=db_context, columns=['COUNTRY_ID', 'COUNTRY_NAME', 'COUNTRY_REGION', 'COUNTRY_REGION_ID'])
    
    if not countries_extract.empty:
        countries_extract['COUNTRY_ID'] = countries_extract['COUNTRY_ID'].astype(int)
        countries_extract['COUNTRY_REGION_ID'] = countries_extract['COUNTRY_REGION_ID'].astype(int)
        countries_extract['ETL_PROCESS_ID'] = etl_process_id
        countries_extract.to_sql(name='COUNTRIES_TRA', con=db_context, if_exists='append', index=False)