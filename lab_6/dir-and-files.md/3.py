import os

def to_check(path):
    if os.path.exists(path):
        print("the path exists.")
        directory = os.path.dirname(path)  
        filename = os.path.basename(path)  

        print(f" Directory: {directory}")
        print(f" Filename: {filename}")

    else:
        print("does not exists")


path = input()
to_check(path)