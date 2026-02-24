import shutil
import os
from copy_contents import copy_contents
from generate_page import generate_pages_recursive

def main():
    static = os.path.abspath("static/")
    public = os.path.abspath("public/")
    template = os.path.abspath("template.html")
    content = os.path.abspath("content")
    if os.path.exists(public):
        shutil.rmtree(public)
    copy_contents(static, public)
    generate_pages_recursive(content, template, public)
    

main()