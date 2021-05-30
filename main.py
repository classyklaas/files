__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os, shutil, zipfile, pathlib
from time import sleep


name_of_file_to_be_created = "cache"
current_working_directory = os.getcwd()
path_to_zip_file = current_working_directory + '/data.zip'
path_to_cache_file = current_working_directory + '/cache'

def clean_cache():
    if os.path.isdir('./cache'):
        print("The file '" + name_of_file_to_be_created + "' already exists. I'm now removing the file and creating an empty, shiny one. One sec please. ")
        shutil.rmtree(path_to_cache_file)
        os.mkdir(name_of_file_to_be_created)
        sleep(5.00)
    else:    
        os.mkdir(name_of_file_to_be_created)
        print("Created new file called '" + name_of_file_to_be_created + "'. One sec please.")
        sleep(5.00)

def cache_zip(zip_file_path, cache_dir_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
        print("Unpacked 999 .txt files and saved them in the file called 'cache'. Going to print them out now. One sec please.")
        sleep(5.00)

def cached_files():
    list_of_lists = [os.path.join(path_to_cache_file, file) for file in os.listdir(path_to_cache_file)]
    return list_of_lists

def find_password(cached_files):
    print('Going to loop through the 999 files and print out a password in case I find one. One sec please')
    sleep(5.00)
    for file in cached_files:
        search_file = open(file, 'r')
        lines = search_file.readlines()
        for line in lines:
            if 'password' in line:
                print('Found one!')
                return line                        

clean_cache()
cache_zip(path_to_zip_file, path_to_cache_file)
print(cached_files())
print(find_password(cached_files()))