import pandas

def generate_etl_process_id(db_context):
    """
    Generate a new ETL_PROCESS_ID
    """
    return db_context.execute('INSERT INTO ETL_PROCESSES VALUES ()').lastrowid

def read_sql_by_process(table_name, columns, etl_process_id, db_context):
    """
    Read data from a table in the database, filtered by ETL_PROCESS_ID
    """
    columns_str = ','.join(columns)
    return pandas.read_sql_query(f'SELECT {columns_str} FROM {table_name} WHERE ETL_PROCESS_ID = {etl_process_id}', db_context)


def get_surrogate_key_from_natural_key(table_name, natural_key_col, natural_key_val, db_context):
    """
    Get the surrogate key value from a natural key (business key)
    """
    return db_context.execute(f'SELECT ID FROM {table_name} WHERE {natural_key_col} = {natural_key_val} LIMIT 1').scalar()
