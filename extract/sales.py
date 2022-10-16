import csv

class Sale:
    def __init__(self, prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold):
        self.prod_id = prod_id
        self.cust_id = cust_id
        self.time_id = time_id
        self.channel_id = channel_id
        self.promo_i = quantity_sold
        self.amount_sold = amount_sold

def compute():
    sales = []
    with open('csv/sales.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sales.append(Sale(row["PROD_ID"],row["CUST_ID"],row["TIME_ID"],row["CHANNEL_ID"],row["PROMO_ID"],row["QUANTITY_SOLD"],row["AMOUNT_SOLD"]))
    return sales
        