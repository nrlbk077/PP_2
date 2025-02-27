def to(s):
    upp = sum(1 for char in s if char.isupper())
    low = sum(1 for char in s if char.islower())
    return upp,low

text = "GYfgesgfsfsfyu&^D^i"
upper_c,lower_c = to(text)
print(f"upper case {upper_c}")
print(f"lower case {lower_c}")