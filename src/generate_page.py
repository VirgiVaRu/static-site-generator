from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path)
    markdown_contents = markdown_file.read()
    markdown_file.close()
    template_file = open(template_path)
    template_contents = template_file.read()
    template_file.close()

    html_node = markdown_to_html_node(markdown_contents)
    html_content = html_node.to_html()
    title = extract_title(markdown_contents)

    final_page = template_contents.replace("{{ Title }}", title)
    final_page = final_page.replace("{{ Content }}", html_content)

    with open(dest_path, "w") as dest:
        dest.write(final_page)
