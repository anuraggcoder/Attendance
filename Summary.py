import numpy as np
import pandas as pd
from datetime import *
import calendar
import shelve

df = pd.read_csv('Employee.csv')

def previousmonth(panchang=False):
    curr_date = datetime.now()

    # Below line replaces day from current date by 1st day of the month(i.e. day=1)
    first_day_of_current_month = curr_date.replace(day=1)
    # The timedelta method, here, takes us 1 day (days=1) before the 1st day
    # of the current month
    last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)

    # Take out year
    previous_month_year = last_day_of_previous_month.year
    # Take out month
    previous_month = last_day_of_previous_month.month

    # Display the calendar for the previous month
    if panchang:
        cal = calendar.month(previous_month_year, previous_month)
        print(cal)

    month_names = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    month = month_names[previous_month]
    number_of_days_in_month = calendar.monthrange(previous_month_year, previous_month)[1]
    return month, number_of_days_in_month

def total_no_of_present():
    previous_month, days = previousmonth()
    mask = df['Month'] == previous_month
    df2 = pd.DataFrame()
    df3 = pd.DataFrame()
    df2 = df[mask].copy()

    db = shelve.open('Employees')
    present_record = {name:0 for name in db}
    for name in db:
        mask2 = df2['Name'] == name
        df3 = df2[mask2].copy()
        for i in df3['Attendance']:
            if i == 'P':
                present_record[name] += 1
        
    for name,presence in present_record.items():
        present_record[name] = '{0:.2f}'.format((present_record[name]/days)*100)
    return present_record
            
if __name__ == '__main__':
    print(total_no_of_present())
    

