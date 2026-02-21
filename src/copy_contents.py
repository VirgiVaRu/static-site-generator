import os
import shutil

def copy_contents(src, dest):
    print(f"{src} is file: {os.path.isfile(src)}")
    if not os.path.exists(dest):
        os.mkdir(dest)
    if os.path.isfile(src):
        shutil.copy(src, dest)
        return
    
    files_to_copy = os.listdir(src)
    print(files_to_copy)
    for file in files_to_copy:
        abspath_file = os.path.join(src, file)
        if os.path.isdir(abspath_file):
            new_dir = os.path.join(dest, file)
            print(f"Creating new directory at {new_dir}")
            os.mkdir(new_dir)
            copy_contents(abspath_file, new_dir)
        else:
            copy_contents(abspath_file, dest)
    return
