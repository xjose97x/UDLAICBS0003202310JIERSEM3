import csv

class Promotion:
    def __init__(self, promo_id, promo_name, promo_cost, promo_begin_date, promo_end_date):
        self.promo_id = promo_id
        self.promo_name = promo_name
        self.promo_cost = promo_cost
        self.promo_begin_date = promo_begin_date
        self.promo_end_date = promo_end_date

def compute():
    promotions = []
    with open('csv/promotions.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            promotions.append(Promotion(row["PROMO_ID"],row["PROMO_NAME"],row["PROMO_COST"],row["PROMO_BEGIN_DATE"],row["PROMO_END_DATE"]))
    return promotions