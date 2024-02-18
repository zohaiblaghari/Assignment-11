def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year,month):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [4,6,9,11]:
        return 30 
    else:
        return 31
    
year = int(input("Enter the year:"))
month = int(input("Enter the month as a number (1-12):"))

if 1 <= month <= 12:
    days_in_month = get_days_in_month(year,month)
    print(f"The number of days in {month}/{year}is:{days_in_month}")
else:
    print("Invalid input. month should be between 1 and 12.")