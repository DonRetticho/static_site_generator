from markdown_blocks import markdown_to_blocks, markdown_to_html_node
import os
from pathlib import Path

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if block.startswith("# "):
            clean_title = block.lstrip("# ").strip()
            return clean_title

    raise Exception("No heading found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown_content = f.read()

    with open(template_path, "r") as d:
        template_content = d.read()

    title = extract_title(markdown_content)
    html_string = markdown_to_html_node(markdown_content).to_html()

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_string)
    template_content = template_content.replace('href="/', 'href="' + basepath)
    template_content = template_content.replace('src="/', 'src="' + basepath)

    directory = os.path.dirname(dest_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(dest_path, "w") as p:
        p.write(template_content)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    folder_list = os.listdir(dir_path_content)
    for item in folder_list:
        full_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(full_path):
            path_obj = Path(dest_path)
            new_path_obj = path_obj.with_suffix(".html")
            generate_page(full_path, template_path, new_path_obj, basepath)
        else:
            generate_pages_recursive(full_path, template_path, dest_path, basepath)
