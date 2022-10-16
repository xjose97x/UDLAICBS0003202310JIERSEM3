from config import StagingProperties
from extract import truncate, extract
from utils.db_connection import Db_Connection


db_context = Db_Connection(
        'mysql', StagingProperties.URL, StagingProperties.PORT, StagingProperties.USER,
        StagingProperties.PASSWORD, StagingProperties.NAME).start()

with db_context.begin(): # transaction
        truncate(db_context)
        extract(db_context)

db_context.dispose()