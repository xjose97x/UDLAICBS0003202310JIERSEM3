from config import StagingProperties
from extract import countries, truncate, extract
from utils.db_connection import Db_Connection


db_context = Db_Connection(
        'mysql', StagingProperties.URL, StagingProperties.PORT, StagingProperties.USER,
        StagingProperties.PASSWORD, StagingProperties.NAME).start()

with db_context.begin(): # transaction
        truncate(db_context)
        extract(db_context)


channels_count = db_context.execute('SELECT COUNT(*) FROM CHANNELS').scalar()
assert channels_count == 5

countries_count = db_context.execute('SELECT COUNT(*) FROM COUNTRIES').scalar()
assert countries_count == 23

customers_count = db_context.execute('SELECT COUNT(*) FROM CUSTOMERS').scalar()
assert customers_count == 55500

products_count = db_context.execute('SELECT COUNT(*) FROM PRODUCTS').scalar()
assert products_count == 72

promotions_count = db_context.execute('SELECT COUNT(*) FROM PROMOTIONS').scalar()
assert promotions_count == 503

sales_count = db_context.execute('SELECT COUNT(*) FROM SALES').scalar()
assert sales_count == 918843

times_count = db_context.execute('SELECT COUNT(*) FROM TIMES').scalar()
assert times_count == 1826

db_context.dispose()

