import time

from . import (channels, countries, customers, products, promotions, sales,
               times)

def load(staging_db_context, core_db_context, etl_process_id):
    start = time.time()
    promotions.load(staging_db_context, core_db_context, etl_process_id)
    times.load(staging_db_context, core_db_context, etl_process_id)
    channels.load(staging_db_context, core_db_context, etl_process_id)
    countries.load(staging_db_context, core_db_context, etl_process_id)
    customers.load(staging_db_context, core_db_context, etl_process_id)
    products.load(staging_db_context, core_db_context, etl_process_id)
    sales.load(staging_db_context, core_db_context, etl_process_id)
    end = time.time()
    print(f"LOAD TOOK: {end - start} seconds")

def tests(db_context):
    channels_count = db_context.execute('SELECT COUNT(*) FROM CHANNELS').scalar()
    assert channels_count == 5, f"Expected 5 channels, got {channels_count}"

    countries_count = db_context.execute('SELECT COUNT(*) FROM COUNTRIES').scalar()
    assert countries_count == 23, f"Expected 23 countries, got {countries_count}"

    customers_count = db_context.execute('SELECT COUNT(*) FROM CUSTOMERS').scalar()
    assert customers_count == 55500, f"Expected 55500 customers, got {customers_count}"

    products_count = db_context.execute('SELECT COUNT(*) FROM PRODUCTS').scalar()
    assert products_count == 72, f"Expected 72 products, got {products_count}"

    promotions_count = db_context.execute('SELECT COUNT(*) FROM PROMOTIONS').scalar()
    assert promotions_count == 503, f"Expected 503 promotions, got {promotions_count}"

    sales_count = db_context.execute('SELECT COUNT(*) FROM SALES').scalar()
    assert sales_count == 918843, f"Expected 918843 sales, got {sales_count}"

    times_count = db_context.execute('SELECT COUNT(*) FROM TIMES').scalar()
    assert times_count == 1826, f"Expected 1826 times, got {times_count}"