import shutil
import os
import sys
from copy_contents import copy_contents
from generate_page import generate_pages_recursive

def main():
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    static = os.path.abspath("static/")
    docs = os.path.abspath("docs/")
    template = os.path.abspath("template.html")
    content = os.path.abspath("content")
    if os.path.exists(docs):
        shutil.rmtree(docs)
    copy_contents(static, docs)
    generate_pages_recursive(content, template, docs, basepath)
    

main()