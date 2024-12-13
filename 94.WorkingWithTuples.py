# Tuples. Tuples are immutable
# Creating tuples
# Empty tuple
empty_tuple = ()
# Tuple wiht mixed data types
person = ("John", 25, "New York")
# Tuple without parentheses
numbers = 1, 2, 3, 4, 5, 6

# Accesssing tuples elements
print(person[0])  # output: "John"
print(person[1])  # output: "25"
print(person[-1])  # output: " New York" (negative indexing)

# Tuple immutability
# numbers[0] = 10  # Raises a TypeError

new_numbers = numbers + (7, 8)
print(new_numbers)  # output: (1, 2, 3, 4, 5, 6, 7, 8)

# Tuple Packing and Unpacking
# Tuple packing
coordinates = 10, 20, 30

# Tuple Unpacking
x, y, z = coordinates
print(x)  # output: 10
print(y)  # output: 20
print(z)  # output: 30

# Tuple Methods
# count(element)
# index(element)
tuple_count = 1, 2, 2, 2, 3, 3, 5
print(tuple_count.count(2))  # Output: 3
print(tuple_count.count(3))  # Output: 2

# Tuple as Return Values
def get_name_and_age():
    name = "Alice"
    age = 25
    return name, age  # is equivalent to return (name, age)

result = get_name_and_age()
print(result)

name, age = get_name_and_age()
print(name)
print(age)