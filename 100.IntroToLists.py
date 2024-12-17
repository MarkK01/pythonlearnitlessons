# declaring a list of numbers
nums = [5, 10, 15.2, 20]
print(nums)

# accessing elements within a list
print(nums[1])  # will output the value at index 1 = 10
num = nums[2]  # saves index value 2 into num
print(num)  # prints value assigned to num

# declaring a list of mixed data types
num = 4.3
data = [num, "word", True]  # the power of data collection
print(data)

# understanding lists within lists
data = [5, "book", [34, "hello"], True]  # Lists can hold any type
print(data)
print(data[2])

# using double bracket notation to access lists within lists
print(data[2][0])  # will output 34
inner_list = data[2]  # inner list will equal [34, 'hello']
print(inner_list[1])  # will output 'hello'

# changing values in a list through index
data = [5, 10, 15, 20]
print(data)
data[0] = 100 # change the value at index 0 - (5 to 100)
print(data)

a = [5, 10]
print(id(a))  # Large number represents location in memory

# understanding how lists are stored
a = [5, 10]
b = a  
print( "a: {}\t b: {}".format(a, b))
print( "Location a[0]: {}\t Location b[0]: {}".format( id(a[0]), id(b[0]) ) )
a[0] = 20  # re-declaring the value of a[0] also changes b[0]
print( "a: {}\t b: {}".format(a, b))

# using [:] to copy a list
# keeps original list intact
data = [5, 10, 15, 20]
data_copy = data[ : ]  # A single colon copies the list
data[0] = 50
print( "data: {}\t data_copy: {}".format(data, data_copy))

