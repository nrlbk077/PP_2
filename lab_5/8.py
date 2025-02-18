import re

with open("row.txt", "r", encoding="utf-8") as file:
    l = file.readlines()  
    
def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

for i in l:
    i = i.strip()
    result = split_at_uppercase(i)
    print(result)
