import os
import re

# Define the regex pattern
pattern = re.compile(r'^.*\.Identifier$')

# Folder path
folder_path = '/home/slajuwomi/Code/ninja-game/data/'

# Walk through all directories and subdirectories
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if pattern.match(filename):
            file_path = os.path.join(root, filename)
            os.remove(file_path)
            print(f'Removed: {file_path}')
