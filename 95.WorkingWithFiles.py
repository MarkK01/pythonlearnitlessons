# Working With Files In Python
# Creating files in write mode
file = open('data.txt', 'w')
# Writing data to the file
file.write('Hello\n')
file.write('world\n')
# Closing files
file.close()
# Opening a file in read mode
file = open('data.txt', 'r')
content = file.read()
print(content)

# Opening a binary file in write mode
binary_file = open('data.bin', 'wb')

# Writing binary data to a file
binary_data = b'\x00\x01\x02\x03'
binary_file.write(binary_data)
binary_file.close()

# Reading binary data from a file
binary_file = open('data.bin', 'rb')
data = binary_file.read()
print(data)

# OPening a Unicode text file with UTF-8 encoding
file = open('unicode.txt', 'w', encoding='utf-8')
file.write('Hello, 世界\n')
file.close()

# Reading a Unicode text file with UTF-8 encoding
file = open('unicode.txt', 'r', encoding='utf-8')
content_unicode = file.read()
print(content_unicode)
