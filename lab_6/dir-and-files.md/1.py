import os

def to_check(path):
    list = os.listdir(path)
    print(list)

path = input()
to_check(path)

