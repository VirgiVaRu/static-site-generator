import shutil
import os
from copy_contents import copy_contents

def main():
    static = os.path.abspath("static/")
    public = os.path.abspath("public/")
    if os.path.exists(public):
        shutil.rmtree(public)
    copy_contents(static, public)

main()