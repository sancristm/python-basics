import calendar
import datetime
import time
print(calendar.weekheader(12))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2021, 12))
print()

print(calendar.monthcalendar(2021, 12))
print(calendar.calendar(2021))

day_of_the_week= calendar.weekday(2021, 12, 3)
print(day_of_the_week) 