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
    print(f"EXTRACT TOOK: {end - start} seconds")


def tests(db_context):
    channels_count = db_context.execute('SELECT COUNT(*) FROM CHANNELS_EXT').scalar()
    assert channels_count == 5, f"Expected 5 channels, got {channels_count}"

    countries_count = db_context.execute('SELECT COUNT(*) FROM COUNTRIES_EXT').scalar()
    assert countries_count == 23, f"Expected 23 countries, got {countries_count}"

    customers_count = db_context.execute('SELECT COUNT(*) FROM CUSTOMERS_EXT').scalar()
    assert customers_count == 55500, f"Expected 55500 customers, got {customers_count}"

    products_count = db_context.execute('SELECT COUNT(*) FROM PRODUCTS_EXT').scalar()
    assert products_count == 72, f"Expected 72 products, got {products_count}"

    promotions_count = db_context.execute('SELECT COUNT(*) FROM PROMOTIONS_EXT').scalar()
    assert promotions_count == 503, f"Expected 503 promotions, got {promotions_count}"

    sales_count = db_context.execute('SELECT COUNT(*) FROM SALES_EXT').scalar()
    assert sales_count == 918843, f"Expected 918843 sales, got {sales_count}"

    times_count = db_context.execute('SELECT COUNT(*) FROM TIMES_EXT').scalar()
    assert times_count == 1826, f"Expected 1826 times, got {times_count}"