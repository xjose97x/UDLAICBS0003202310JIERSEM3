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


def get_surrogate_key_and_natural_key_pairs(table_name, natural_key_col, db_context):
    """
    Get the surrogate key value from a natural key (business key)
    """
    return pandas.read_sql_query(f'SELECT ID, {natural_key_col} FROM {table_name}', db_context).set_index(natural_key_col).to_dict()['ID']
