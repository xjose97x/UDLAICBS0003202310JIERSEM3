from . import countries, customers, products, sales, times, promotions, channels

def truncate(db_context):
    sales.truncate(db_context)
    customers.truncate(db_context)
    channels.truncate(db_context)
    countries.truncate(db_context)
    products.truncate(db_context)
    times.truncate(db_context)

def extract(db_context):
    promotions.run(db_context)
    times.run(db_context)
    channels.run(db_context)
    countries.run(db_context)
    customers.run(db_context)
    products.run(db_context)
    sales.run(db_context)