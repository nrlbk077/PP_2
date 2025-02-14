from datetime import datetime, timedelta

x = datetime.now()

y = timedelta(days=1)

date = x - y
data = x + y
print("Today:", x.strftime('%Y-%m-%d'))
print("Yesterday:", date.strftime('%Y-%m-%d'))
print("Tomorrow:", data.strftime('%Y-%m-%d'))