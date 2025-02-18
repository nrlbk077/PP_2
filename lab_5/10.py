import re

with open("row.txt", "r", encoding="utf-8") as file:
    l = file.readlines()

def to_snake(camel_str):
    snake_str = re.sub(r'([A-Z])', r'_\1', camel_str).lower()
    if snake_str[0] == '_':
        snake_str = snake_str[1:]
    return snake_str

for i in l:
    i = i.strip() 
    snake_case = to_snake(i)
    print(snake_case)
