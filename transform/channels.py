import pandas

def transform(db_context, etl_process_id):
    channels_extract = pandas.read_sql_table(table_name='CHANNELS_EXT', con=db_context, columns=['CHANNEL_ID', 'CHANNEL_DESC', 'CHANNEL_CLASS', 'CHANNEL_CLASS_ID'])
    

    if not channels_extract.empty:
        channels_extract['CHANNEL_ID'] = channels_extract['CHANNEL_ID'].astype(int)
        channels_extract['CHANNEL_CLASS_ID'] = channels_extract['CHANNEL_CLASS_ID'].astype(int)
        channels_extract['ETL_PROCESS_ID'] = etl_process_id
        channels_extract.to_sql(name='CHANNELS_TRA', con=db_context, if_exists='append', index=False)