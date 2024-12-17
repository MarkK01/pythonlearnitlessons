number_guess = "0"
secret_number = "5"

while True:
    number_guess = input("guess the number 1 to 5: ")
    if number_guess == secret_number:
        print("Yes", number_guess, "is correct!\n")
        break
    else:
        print(number_guess, "is incorrect\n")


while True:
    f_name = input("enter a single word first name: ")

    if f_name.isalpha():
        break
    else:
        print(f_name, "is not a single word\n")

        print("Welcome", f_name + "!")