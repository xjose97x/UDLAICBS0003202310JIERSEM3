import time

from . import (channels, countries, customers, products, promotions, sales,
               times)


def truncate(db_context):
    start = time.time()
    sales.truncate(db_context)
    customers.truncate(db_context)
    channels.truncate(db_context)
    countries.truncate(db_context)
    products.truncate(db_context)
    times.truncate(db_context)
    promotions.truncate(db_context)
    end = time.time()
    print(f"TRUNCATE TOOK: {end - start} seconds")


def extract(db_context):
    start = time.time()
    promotions.run(db_context)
    times.run(db_context)
    channels.run(db_context)
    countries.run(db_context)
    customers.run(db_context)
    products.run(db_context)
    sales.run(db_context)
    end = time.time()
    print(f"INSERT TOOK: {end - start} seconds")
