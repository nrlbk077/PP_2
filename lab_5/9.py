import re

with open("row.txt", "r", encoding="utf-8") as file:
    l = file.readlines()

def insert_spaces(text):
    return re.sub(r'(?<=[a-z])([A-Z])', r' \1', text)

for i in l:
    i = i.strip() 
    
    result = insert_spaces(i)
    print(result)
