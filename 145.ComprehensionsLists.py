# Comprehension
# Comprehensions are a concise and powerful feature in Python that allow you to create new lists by applying
# an expression to each item in a sequence.
# This sequence can be any iterable such as a list tuple or even a range.

# Suppose we have a list of students and their exam scores(tuples)
students = [
    ('Alice', 85, 90),
    ('Bob', 70, 78),
    ('Charlie', 92, 88)
]

# We want to extract the second column, which represents their midterm scores
#
# The comprehension starts with an opening square bracket to create a new list.
# The expression number plus one adds one to each number.
# Number in the numbers list.
# The for numbering numbers part iterates over each number in the numbers list.
# The variable number takes on each number's value one by one.
# The comprehension ends with a closing square bracket.
# After executing the comprehension, the result is a new list named increment underscore numbers that
# contains the original numbers increment by one.
midterm_scores = [student[1] for student in students]   #second column is student[1]
print(midterm_scores)

# List of numbers
numbers = [2, 5, 8]

# Add 1 to each number using a list comprehension
incremented_numbers = [num + 1 for num in numbers]
print(incremented_numbers)

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter out odd numbers using a list comprehension and the % operator
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


# Generate a list of squares an cubes of numbers from 0 to 3
squares_and_cubes = [[x ** 2, x ** 3] for x in range(4)]

# Output the list of squares and cubes
print(squares_and_cubes)  # Output: [[0, 0], [1, 1], [4, 8], [9, 27]]


# Create a list of even numbers, their halves, and doubles using a condition
even_and_related = [[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]

# Output the list of event numbers and related values
print(even_and_related)  # Output: [[2, 1.0, 4], [4, 2.0, 8], [6, 3.0, 12]]