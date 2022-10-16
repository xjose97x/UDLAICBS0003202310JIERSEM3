import csv

class Country:
    def __init__(self, country_id, country_name, country_region, country_region_id):
        self.country_id = country_id
        self.country_name = country_name
        self.country_region = country_region
        self.country_region_id = country_region_id

def compute():
    countries = []
    with open('csv/countries.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            countries.append(Country(row['COUNTRY_ID'], row['COUNTRY_NAME'], row['COUNTRY_REGION'], row['COUNTRY_REGION_ID']))
    return countries