import calendar, datetime

print(datetime.date.today())
print(datetime.timedelta(days=1))

today = datetime.date.today()
first_of_month = today.replace(day=1)
last_day_last_month = first_of_month - datetime.timedelta(days=1)
mdays = calendar.monthrange(last_day_last_month.year, last_day_last_month.month)[1]

print(today)
print(first_of_month)
print(last_day_last_month)
print(mdays)
