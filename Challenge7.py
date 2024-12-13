import calendar

year = int(input("Year: "))
month = int(input("Month: "))

cal = calendar.month(year, month)

print(cal)