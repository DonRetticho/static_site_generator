import os
import shutil

def copy_files_recursive(source_dir, destination_dir):    
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)

    for item in os.listdir(source_dir):
        full_path = os.path.join(source_dir, item)
        dest_path = os.path.join(destination_dir, item)

        if os.path.isfile(full_path):
            print(f"Found a file: {full_path}")
            shutil.copy(full_path, dest_path)
        else:
            print(f"Entering directory: {full_path}")
            copy_files_recursive(full_path, dest_path)