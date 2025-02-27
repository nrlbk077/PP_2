def count_lines(path):
    
    with open(path, 'r') as file:
        line_count = sum(1 for _ in file)
    print(f"The file has {line_count} lines.")
   
path = input()

count_lines(path)


#C:\Users\NRLBK\Desktop\PP_2_NRLBK\lab_6\dir-and-files.md\row.txt