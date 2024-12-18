# Handling Absolute and Relative Paths
import os

# os.path.join()
# os.path.abspath()   # returns full path
# os.path.isabs()
# os.path.relpath()   # returns relative path
# os.path.abspath(".")
# os.path.abspath('./scripts')
# os.path.isabs('.')
# os.path.isabs(os.path.abspath('.'))

os.path.relpath('c:\\windows', 'c:\\')
os.path.relpath('c:\\windows', 'c:\\py')
os.getcwd()
path = 'c:\\windows\\system32\\calc.exe'
os.path.basename(path)
os.path.dirname(path)
calcFilePath = 'c:\\windows\\system32\\calc.exe'
os.path.split(calcFilePath)
(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
print(calcFilePath.split(os.path.sep))

# Get size of file
# os.path.getsize()
absfile = os.path.getsize('C:\\Users\\mark.knesek\\Downloads\\20241216_01000007.csv')
print(absfile)

# List contents of directory
# os.listdir()
zDir = os.listdir('C:\\Ziosk')
print(zDir)

# totalSize = 0
# for filename in os.listdir('c:\\Ziosk'):
#     totalSize = totalSize + os.path.getsize(os.path.join('c:\\Ziosk', filename))   # os.path.join() joins pathname with filename
#     print(totalSize)

# Check if file / directory exists  -- Returns True or false
os.path.exists('c:\\folder_name')
os.path.isdir('c:\\directory')
os.path.isfile('c:\\filename')

# Working with Files
# 3 steps to working with files
# 1. open file 2. read file 3. close file

file1 = open('c:\\temp\\file1.txt', 'r')   # 'r' option is default
fileContent = file1.read()
print(fileContent)
file1.close()

file2 = open('c:\\temp\\file1.txt')
file2Content = file2.readlines()  # readlines() reads entire file
print(file2Content)
file2.close()

file3 = open('c:\\temp\\file3.txt', 'w')   # overwrites file
file3.write("Hello World!\n")
file3.close()
file3 = open('c:\\temp\\file3.txt', 'a')   # appends to end of file
file3.write("Appended a line!\n")
file3.close()

file3 = open('c:\\temp\\file3.txt')
file3Content = file3.readlines()  # readlines() reads entire file
print(file3Content)
file3.close()

# remove a file
# file3 = 'c:\\temp\\file3.txt'
# os.remove(file3)

file3 = input("Please specify the file to remove: ")

# if file exists, delete it
if os.path.isfile(file3):
    os.remove(file3)
    print("File: %s removed" % file3)
else:
    print("Error: %s file not found" % file3)


