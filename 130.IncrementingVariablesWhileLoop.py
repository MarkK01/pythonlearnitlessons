# Increment a Variable
seat_count = 0

while True:
    seat_count = seat_count + 1
    print("seat count:", seat_count)
    if seat_count >= 4:
        print("no seats remaining")
        break

# Decrementing a Variable
seat_count = 4

while True:
    print("remaining seat count:", seat_count)
    seat_count = seat_count - 1

    if seat_count <= 0:
        print("Final reamining seat count:", seat_count)
        break

greet_count = 5

while greet_count > 0:
    print(greet_count, "!")
    greet_count -= 1

print("\nIGNITION!")


# No spaces in name input
student_fname = ""
while student_fname.isalpha() == False:
    student_fname = input("enter first name (letters, no spaces): ")

print("\n" + student_fname.title(), "has been entered as a first name")

# Wants all Capital Letters as input
message = "hi"
while message.isupper() != True:
    message = input("Sorry, can\'t hear, please yell message: ")

print('message: "' + message + '" received')


number = ""
while number.isdigit() != True:
    number = input("enter a positive integer: ")

print(number, "is an integer")
