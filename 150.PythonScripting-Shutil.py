# shutil module
# provide functions for copying files and folders

import os
import shutil
os.chdir('c:\\temp')
shutil.copy('c:\\temp\file3.txt', 'c:\\temp\file4.txt')

shutil.copytree('c:\\temp', 'c:\\tmp')

shutil.move('c:\\temp\file1.txt' 'c:\\temp\file5.txt')