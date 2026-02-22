import os
import shutil
from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive
import sys

source_dir = "./static"
destination_dir = "./docs"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)


    print("Copying static files to public directory...")
    copy_files_recursive(source_dir, destination_dir)

    print("Generating content...")
    #generate_page("./content/index.md", "./template.html", "./public/index.html")
    generate_pages_recursive("./content", "./template.html", destination_dir, basepath)
main()