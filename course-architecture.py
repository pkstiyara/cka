
# This code is used to create the complete folder architecture for 100days learning 


import os

for i in range(1, 101):
    folder_name = f"Day-{i}"
    file_name = f"{folder_name}.md"

    # Create the folder
    os.mkdir(folder_name)

    # Create and write to the markdown file
    with open(os.path.join(folder_name, file_name), 'w') as file:
        file.write(f"# {folder_name}\n\nThis is the content of {file_name}.")
