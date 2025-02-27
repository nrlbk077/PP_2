import os
def to_delete(path):
    if os.path.exists(path):
        if os.access(path, os.R_OK) and os.access(path, os.W_OK):
            os.remove(path)
            print(f"Deleted")
        else:
            print("Error")
    else:
        print("Error")


path = input()
to_delete(path)
#C:\Users\NRLBK\Desktop\PP_2_NRLBK\lab_6\dir-and-files.md\D.txt