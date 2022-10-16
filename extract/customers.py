import csv

class Customer:
    def __init__(self, cust_id, cust_first_name, cust_last_name, cust_gender, cust_year_of_birth, cust_marital_status, cust_street_address, cust_postal_code, cust_city, cust_state_province, country_id, cust_main_phone_number, cust_income_level, cust_credit_limit, cust_email):
        self.cust_id = cust_id
        self.cust_first_name = cust_first_name
        self.cust_last_name = cust_last_name
        self.cust_gender = cust_gender
        self.cust_year_of_birth = cust_year_of_birth
        self.cust_marital_status = cust_marital_status
        self.cust_street_address = cust_street_address
        self.cust_postal_code = cust_postal_code
        self.cust_city = cust_city
        self.cust_state_province = cust_state_province
        self.country_id = country_id
        self.cust_main_phone_number = cust_main_phone_number
        self.cust_income_level = cust_income_level
        self.cust_credit_limit = cust_credit_limit
        self.cust_email = cust_email

def compute():
    customers = []
    with open('csv/customers.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            customers.append(Customer(row["CUST_ID"],row["CUST_FIRST_NAME"],row["CUST_LAST_NAME"],row["CUST_GENDER"],row["CUST_YEAR_OF_BIRTH"],row["CUST_MARITAL_STATUS"],row["CUST_STREET_ADDRESS"],row["CUST_POSTAL_CODE"],row["CUST_CITY"],row["CUST_STATE_PROVINCE"],row["COUNTRY_ID"],row["CUST_MAIN_PHONE_NUMBER"],row["CUST_INCOME_LEVEL"],row["CUST_CREDIT_LIMIT"],row["CUST_EMAIL"]))
    return customers