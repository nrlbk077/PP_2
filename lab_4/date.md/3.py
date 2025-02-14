from datetime import datetime

now = datetime.now()
print("Original datetime:", now)

now_without_microseconds = now.replace(microsecond=0)
print("Datetime without microseconds:", now_without_microseconds)