# Index Slicing [start:stop]
student_name = "Colette"
print("slide student_name[2:5]:", student_name[2:5])  # output:  slide student_name[2:5]: let
print("index 2, 3 & 4 of student_name: ", student_name[2] + student_name[3] + student_name[4])  # output:  index 2, 3 & 4 of student_name: let

long_word = 'Acknowledgement'
print(long_word, "\n")
print(long_word[2:11])
print(long_word[2:11], "is the 3rd char through the 11th char")  # output: knowledge is the 3rd char through the 11th char
print(long_word[2:11], "is the index 2, \"" + long_word[2] + "\",", "through index 10, \"" + long_word[10] + "\"")  # output: knowledge is the index 2, "k", through index 10, "e"

# Index Slicing [:stop]
# default start for a slice is index 0
student_name = "Colette"
print(student_name[:3])  # Output: Col

# Accessing sub-strings by step size
# Index slicing[::2]
long_word = "Consequences"
print(long_word, "\n")
print(long_word[1:9:2])  # output: osqe