def is_palindrome(s):
    return s == s[::-1]  

string = input()
if is_palindrome(string):
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")