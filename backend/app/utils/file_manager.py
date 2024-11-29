import os
import shutil

def save_file(file, location):
    file_path = None
    try:
        file_path = os.path.join(location, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        
    except Exception as e:
        raise RuntimeError(f"Error saving file: {e}")
    return file_path

def cleanup(dir_name):
    try:
        shutil.rmtree(dir_name)
    except Exception as e:
        raise RuntimeError(f"Error cleaning up files: {e}")
    
    return True