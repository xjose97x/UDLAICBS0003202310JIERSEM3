import time
from . import (channels, countries, customers, products, promotions, sales,
               times)


def transform(db_context, etl_process_id):
    start = time.time()
    promotions.transform(db_context, etl_process_id)
    times.transform(db_context, etl_process_id)
    channels.transform(db_context, etl_process_id)
    countries.transform(db_context, etl_process_id)
    customers.transform(db_context, etl_process_id)
    products.transform(db_context, etl_process_id)
    sales.transform(db_context, etl_process_id)
    end = time.time()
    print(f"INSERT TOOK: {end - start} seconds")
