import os

def to_check(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Readable:", os.access(path, os.R_OK))
        print("Writable:", os.access(path, os.W_OK))
        print("Executable:", os.access(path, os.X_OK))
    else:
        print("does not exists")


path = input()
to_check(path)