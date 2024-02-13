
import os

directory = os.getcwd()
files = os.listdir(directory)

def list_files_by_extension(extension):

    # Filter files with the given extension
    filtered_files = [file for file in files if file.endswith("." + extension)]

    if filtered_files:
        print("Files with extension .{} in the current directory:".format(extension))
        for file in filtered_files:
            print(file)
    else:
        print("No files with extension .{} found in the current directory.".format(extension))

def rename_files(extension):

    # Filter
    sort_files = [file for file in files if file.endswith("." + extension)]

    # Sort the files
    sort_files.sort()

    # Rename and move the files
    for i, file in enumerate(sort_files):
        # Generate the new filename
        new_filename = f"{i+1:03}." + extension # :03 for 000; remove it then will start from 0
        
        # Rename the file
        os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))
        
        print(f"Renamed {file} to {new_filename}")

file_extension = input("Enter file extension (e.g., txt, pdf, jpg): ").strip().lower()
list_files_by_extension(file_extension)

user_input = input("Rename those file(s)? (Y/n) ")
if user_input.lower()=="y":
    rename_files(file_extension)
else: print("Cancelled.")
