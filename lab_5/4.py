import re

patt = r"^ab*$"

with open("row.txt", "r", encoding="utf-8") as file:
    l = file.readlines()

for i in l:
    i = i.strip()  
    if not re.fullmatch(patt, i):
        print(f"Matched: {i}")
    else:
        print(f"Not Matched: {i}")
