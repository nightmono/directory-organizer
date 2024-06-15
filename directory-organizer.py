import os
import shutil
import sys

def move_to_dir(path: str, dirs: list, dir_name: str, file: str):
    if dir_name not in dirs:
        os.mkdir(os.path.join(path, dir_name))
        dirs.append(dir_name)
    
    file_path = os.path.join(path, file)
    dir_path = os.path.join(path, dir_name)
    new_dest = os.path.join(dir_path, file)
    
    shutil.move(file_path, new_dest)
    print(f"Moved {file_path} to {new_dest}")

def organise(path="."):
    _, dirs, files = next(os.walk(path))
    
    for file in files:
        parts = file.split(".")

        # Realistically, parts length should always be at least 1.
        if len(parts) < 2:
            move_to_dir(path, dirs, "no-file-ext", file)
        else:
            move_to_dir(path, dirs, parts[-1], file)
            
if __name__ == "__main__":
    args = sys.argv
    
    if len(args) > 1:
        path = args[1]
    
    organise(path)