from datetime import datetime, timedelta

date = input("Enter a date (YYYY-MM-DD): ")
days = int(input("Enter number of days to add: "))

d = datetime.strptime(date, "%Y-%m-%d")
new_date = d + timedelta(days=days)

print("New date:", new_date.strftime("%Y-%m-%d"))