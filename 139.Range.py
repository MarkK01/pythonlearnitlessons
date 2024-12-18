# Range

# range(stop) - function to create a numeric sequence
range(10)
for count in range(10):
    print(count)

# variables can be initialized with range objects and used in iteration
digits = range(10)
print("digits =", list(digits), "\n")
sub_total = 0

for item in digits:
    sub_total += item
    print("sub_total:", sub_total)
print("Total =", sub_total)

# range() used in iterating a list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar"]
half_1 = int(len(spell_list)/2)
print("half way = ", half_1, "\n")

for word in range(half_1):
    print(spell_list[word])

# range(start,stop)

for count in range(5,10):
    print(count)

sub_total = 0 
temp = 0

for item in range(5, 11):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=", sub_total)

print("Total = ", sub_total)

# use range(start, stop) to print 2nd half of a list of strings
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar"]
spell_len = len(spell_list)
half_1 = int(spell_len/2)
print("half 1 = ", half_1, "\n")

for word in range(half_1,spell_len):
    print(spell_list[word])

#
# Range(Start,Stop,Step)
#
# Example 1: Counting sequence with a step of 25
for i in range(25, 101, 25):
    print(i)

# Example 2: Summing up a counting sequence with a step of 5
total = 0
for i in range(25, 46, 5):
    print(i)
    total += i
print("Total:", total)

# Example 3: Printing every other word in a list
words = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(0, len(words), 2):
    print(words[i])

