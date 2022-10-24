from utils import query_utils

def load(staging_db_context, core_db_context, etl_process_id):
    channels = query_utils.read_sql_by_process(table_name='CHANNELS_TRA', columns=['CHANNEL_ID', 'CHANNEL_DESC', 'CHANNEL_CLASS', 'CHANNEL_CLASS_ID'], etl_process_id=etl_process_id, db_context=staging_db_context)
    channels.to_sql('CHANNELS', core_db_context, if_exists='append', index=False)