from utils.db_connection import Db_Connection


class DbClient:
    def __init__(self):
        self.db_connection = Db_Connection.start()

    def execute(self, query):
        self.db_connection.execute(query)

    def truncate(self, table):
        self.execute(f"TRUNCATE TABLE {table}")
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.db_connection.dispose()
    