def get_days_in_month(month):
    if month == 2:
        return 28
    elif month in [4,6,9,11]:
        return 30
    else:
        return 31

month = int(input("Enter the month as a number (1-12):"))
if 1 <= month <= 12:
    days_in_month = get_days_in_month(month)
    print(f"The number of days in month {month} is: {days_in_month}")
else:
    print("Invalid input. Month should be between 1 and 12.")