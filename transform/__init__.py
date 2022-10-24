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
    print(f"TRANSFORM TOOK: {end - start} seconds")


def tests(db_context, etl_process_id):
    channels_count = db_context.execute(f'SELECT COUNT(*) FROM CHANNELS_TRA WHERE ETL_PROCESS_ID = {etl_process_id}').scalar()
    assert channels_count == 5, f"Expected 5 channels, got {channels_count}"

    countries_count = db_context.execute(f'SELECT COUNT(*) FROM COUNTRIES_TRA WHERE ETL_PROCESS_ID = {etl_process_id}').scalar()
    assert countries_count == 23, f"Expected 23 countries, got {countries_count}"

    customers_count = db_context.execute(f'SELECT COUNT(*) FROM CUSTOMERS_TRA WHERE ETL_PROCESS_ID = {etl_process_id}').scalar()
    assert customers_count == 55500, f"Expected 55500 customers, got {customers_count}"

    products_count = db_context.execute(f'SELECT COUNT(*) FROM PRODUCTS_TRA WHERE ETL_PROCESS_ID = {etl_process_id}').scalar()
    assert products_count == 72, f"Expected 72 products, got {products_count}"

    promotions_count = db_context.execute(f'SELECT COUNT(*) FROM PROMOTIONS_TRA WHERE ETL_PROCESS_ID = {etl_process_id}').scalar()
    assert promotions_count == 503, f"Expected 503 promotions, got {promotions_count}"

    sales_count = db_context.execute(f'SELECT COUNT(*) FROM SALES_TRA WHERE ETL_PROCESS_ID = {etl_process_id}').scalar()
    assert sales_count == 918843, f"Expected 918843 sales, got {sales_count}"

    times_count = db_context.execute(f'SELECT COUNT(*) FROM TIMES_TRA WHERE ETL_PROCESS_ID = {etl_process_id}').scalar()
    assert times_count == 1826, f"Expected 1826 times, got {times_count}"