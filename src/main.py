import shutil
import os
from copy_contents import copy_contents
from generate_page import generate_page

def main():
    static = os.path.abspath("static/")
    public = os.path.abspath("public/")
    if os.path.exists(public):
        shutil.rmtree(public)
    copy_contents(static, public)
    generate_page("content/index.md", "template.html", "public/index.html")
    

main()