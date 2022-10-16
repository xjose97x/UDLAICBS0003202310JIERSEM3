import csv

class Product:
    def __init__(self, prod_id, prod_name, prod_desc, prod_category, prod_category_id, prod_category_desc, prod_weight_class, supplier_id, prod_status, prod_list_price, prod_min_price):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.prod_desc = prod_desc
        self.prod_category = prod_category
        self.prod_category_id = prod_category_id
        self.prod_category_desc = prod_category_desc
        self.prod_weight_class = prod_weight_class
        self.supplier_id = supplier_id
        self.prod_status = prod_status
        self.prod_list_price = prod_list_price
        self.prod_min_price = prod_min_price

def compute():
    products = []
    with open('csv/products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(Product(row["PROD_ID"],row["PROD_NAME"],row["PROD_DESC"],row["PROD_CATEGORY"],row["PROD_CATEGORY_ID"],row["PROD_CATEGORY_DESC"],row["PROD_WEIGHT_CLASS"],row["SUPPLIER_ID"],row["PROD_STATUS"],row["PROD_LIST_PRICE"],row["PROD_MIN_PRICE"]))
    return products