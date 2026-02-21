from textnode import TextNode, TextType
import os
import shutil
from copystatic import copy_files_recursive

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")

    source_dir = "static"
    destination_dir = "public"

    copy_files_recursive(source_dir, destination_dir)

    # node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # print(node)

main()