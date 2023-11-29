import calendar

def print_year_calendar(year):
    for month in range(1, 13):
        print(calendar.month(year, month))

# Replace 2023 with the desired year
print_year_calendar(2023)
