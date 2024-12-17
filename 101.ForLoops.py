# For Loops

# writing your first for Loop using range
for num in range(5):
    print("Value: {}".format(num))

# providing the start, stop, and step for the range function
for num in range(2, 10, 2):
    print( "Value: {}".format(num))  # will print all evens between 2 and 10

# print all characters in a name using the 'in' keyword
name = "John Smith"
for letter in name:
    print("Value: {}".format(letter))

# using the continue statement within a for loop
for num in range(5):
    if num == 3:
        continue
    print(num)

# breaking out of a Loop using the "break" keyword
# double loops - break will only break out of current loop
for num in range(5):
    if num == 3:
        break
    print(num)

# setting a placeholder using the 'pass' keyword
for i in range(5):
    pass    # TODO:  Add code to print number

# Practice
# 1. Write a for loop that prints all numbers from 1 to 100 divisible by 3
print("\nThese are numbers from 1 to 100 divided by 3")
for num in range(1, 100):
    if ( num % 3 ) == 0:
        print(num)


# 2. Ask for user input of a sentence and print out all of the vowels in the phrase
sentence = input("Type in a sentence and press enter: ")
for vowel in sentence:
    if vowel in ['a', 'e', 'i', 'o', 'u']:
        print("Value: {}".format(vowel))
