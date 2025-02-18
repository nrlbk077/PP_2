import re


with open("row.txt", "r", encoding="utf-8") as file:
    l = file.readlines()
    
def to_camel(snake_str):
    words = snake_str.split('_')
    camel_case_str = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_str

for i in l:
    i = i.strip() 
    camel_case = to_camel(i)
    print(camel_case)

