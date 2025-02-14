from datetime import datetime, timedelta

x = datetime.now()

y = timedelta(days=5)
date = x - y

print("Current Date:", x.strftime('%Y-%m-%d'))
print("After 5 days:", date.strftime('%Y-%m-%d'))
