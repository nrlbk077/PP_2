import re

patt = r"^ab*$"

with open("row.txt", "r") as file:
    l = file.readlines()

for i in l:
    i = i.strip()  
    if re.fullmatch(patt, i):
        print(f"Matched: {i}")
    else:
        print(f"Not Matched: {i}")
