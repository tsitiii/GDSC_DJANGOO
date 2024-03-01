import os
import time
import shutil

files = os.listdir()
print(files)

def check_for_file(file):
    if os.path.isfile(file):
        file_status = os.stat(file)
        current_time = time.time()
        mod_time_diff = current_time - file_status.st_mtime
        creation_time_diff = current_time - file_status.st_ctime

        if mod_time_diff < 24 * 60 * 60 or creation_time_diff < 24 * 60 * 60:
            return True
        else:
            return False
    else: return False

def update_files(files):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    for file in files:
        with open(file, 'a') as file_obj:
            file_obj.write(f"\nUpdated at: {timestamp}")

def move_files(files, destin_folder):
    if not os.path.exists(destin_folder):
        os.mkdir(destin_folder)

    for file in files:
        destination_path = os.path.join(destin_folder, os.path.basename(file))
        shutil.move(file, destination_path)

current_directory = os.getcwd()
files = [os.path.join(current_directory, file) for file in files]
recent_files = [file for file in files if check_for_file(file)]
update_files(recent_files)
destin_folder = os.path.join(current_directory, "last_24hours")
move_files(recent_files, destin_folder)
