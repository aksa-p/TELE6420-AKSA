from datetime import datetime
from datetime import date
import calendar
time_now = datetime.now()
time_current = time_now.strftime("%H:%M:%S")
date_c = date.today()

print("The current time is ", time_current)
print("The current date is", time_now.date())
print(calendar.day_name[date_c.weekday()])
