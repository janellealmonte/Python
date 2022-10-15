#!/usr/bin/env python3

from datetime import date

def calculate_age(birthdate):
    str_day, str_month, str_year = birthdate.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    birthdate=date(year,month,day)
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
if __name__ == '__main__':   # This section also referred to as a "main block"
    birthdate=input('Input birthdate (dd-mm-yyyy):')
    
    print(calculate_age(birthdate))
