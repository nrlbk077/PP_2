def copy_file(source_path, destination_path):

    with open(source_path, 'r') as src_file:
        content = src_file.read() 

    with open(destination_path, 'w') as dest_file:
        dest_file.write(content)  
        
    print(f"Successfully copied '{source_path}' to '{destination_path}'.")
   
source = input()
destination = input()


copy_file(source, destination)
