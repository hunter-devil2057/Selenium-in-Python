import datetime

# get the current date and time
date = datetime.datetime.now()
date = datetime.date.today()
print(date)

print(f"Current Year, ", date.year)
print(f"Current Month, ", date.month)
print(f"Current Day, ", date.day)

print(dir(datetime))