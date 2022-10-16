import csv

class Time:
    def __init__(self, time_id, day_name, day_number_in_week, day_number_in_month, calendar_week_number, calendar_month_number, calendar_month_desc, end_of_cal_month, calendar_quarter_desc, calendar_year):
        self.time_id = time_id
        self.day_name = day_name
        self.day_number_in_week = day_number_in_week
        self.day_number_in_month = day_number_in_month
        self.calendar_week_number = calendar_week_number
        self.calendar_month_number = calendar_month_number
        self.calendar_month_desc = calendar_month_desc
        self.end_of_cal_month = end_of_cal_month
        self.calendar_quarter_desc = calendar_quarter_desc
        self.calendar_year = calendar_year

def compute():
    times = []
    with open('csv/times.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            times.append(Time(row["TIME_ID"],row["DAY_NAME"],row["DAY_NUMBER_IN_WEEK"],row["DAY_NUMBER_IN_MONTH"],row["CALENDAR_WEEK_NUMBER"],row["CALENDAR_MONTH_NUMBER"],row["CALENDAR_MONTH_DESC"],row["END_OF_CAL_MONTH"],row["CALENDAR_QUARTER_DESC"],row["CALENDAR_YEAR"]))
    return times