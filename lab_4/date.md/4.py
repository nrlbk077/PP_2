from datetime import datetime

def date_difference_in_seconds(date1: str, date2: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> int:
    
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    
    return abs(int((d2 - d1).total_seconds()))


date1 = "2025-02-10 12:30:45"
date2 = "2025-02-11 14:45:30"
diff_seconds = date_difference_in_seconds(date1, date2)
print(f"Difference in seconds: {diff_seconds}")