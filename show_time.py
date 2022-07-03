from datetime import datetime
time_now = datetime.now()
time_current = time_now.strftime("%H:%M:%S")
print("The current time is ", time_current)
