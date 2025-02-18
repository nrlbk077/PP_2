import re

patt = r"^a.*b$"

with open("row.txt", "r", encoding="utf-8") as file:
    l = file.readlines()

for i in l:
    i = i.strip() 
    new_text = re.sub(r"[_ ,.]","_",i, flags=re.IGNORECASE) 
    print(new_text)   
    