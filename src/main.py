import os
import shutil
from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

source_dir = "./static"
destination_dir = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists("public"):
        shutil.rmtree("public")


    print("Copying static files to public directory...")
    copy_files_recursive(source_dir, destination_dir)

    print("Generating content...")
    #generate_page("./content/index.md", "./template.html", "./public/index.html")
    generate_pages_recursive("./content", "./template.html", "./public")
main()