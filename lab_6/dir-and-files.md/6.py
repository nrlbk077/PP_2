def create_files():
    for i in range(65, 91):  
        file_name = f"{chr(i)}.txt"  
        with open(file_name, 'w') as file:
            file.write(f"This is {file_name}\n")  
        print(f"Created: {file_name}")

create_files()
