# Iterate a String: 1 Character at time
word = "cello"
for letter in word:
    print(letter)

student_name = "Skye"
new_name = ""

for ltr in student_name:
    if ltr.lower() == "y":
        new_name += ltr.upper()
    else:
        new_name += ltr

print(student_name, "to", new_name)

