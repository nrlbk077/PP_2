def write_to_file(path, data_list):
    
    with open(path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")  
    print(f"The list written")


data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

path = input()

write_to_file(path, data)
