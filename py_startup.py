from config import StagingProperties
from extract import truncate, extract
from transform import transform
from utils.db_connection import Db_Connection
from utils import query_utils


db_context = Db_Connection(
        'mysql', StagingProperties.URL, StagingProperties.PORT, StagingProperties.USER,
        StagingProperties.PASSWORD, StagingProperties.NAME).start()

with db_context.begin(): # transaction
        truncate(db_context)
        extract(db_context)
        etl_process_id = query_utils.generate_etl_process_id(db_context)
        transform(db_context, etl_process_id)


channels_count = db_context.execute('SELECT COUNT(*) FROM CHANNELS_EXT').scalar()
assert channels_count == 5

countries_count = db_context.execute('SELECT COUNT(*) FROM COUNTRIES_EXT').scalar()
assert countries_count == 23

customers_count = db_context.execute('SELECT COUNT(*) FROM CUSTOMERS_EXT').scalar()
assert customers_count == 55500

products_count = db_context.execute('SELECT COUNT(*) FROM PRODUCTS_EXT').scalar()
assert products_count == 72

promotions_count = db_context.execute('SELECT COUNT(*) FROM PROMOTIONS_EXT').scalar()
assert promotions_count == 503

sales_count = db_context.execute('SELECT COUNT(*) FROM SALES_EXT').scalar()
assert sales_count == 918843

times_count = db_context.execute('SELECT COUNT(*) FROM TIMES_EXT').scalar()
assert times_count == 1826

db_context.dispose()

