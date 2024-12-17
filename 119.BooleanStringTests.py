# Return Boolean True or False methods
# .alpha()
# .isalnum()
# .istitle()
# .isdigit()
# .islower()
# .isupper()
#.startswith()

print("Hello".isalpha())   # Outputs: TRUE

print("Python!".isalpha())  # Outputs FALSE

print("3rd".isalnum())  # Outputs TRUE

print("A Cold Stormy Night".istitle())  # Outputs TRUE

print("1003".isdigit())  # Outputs TRUE

cm_height = "176"
print(cm_height.isdigit())  # Outputs TRUE
print("cm height:", cm_height, "is all digits = ", cm_height.isdigit())

print("SAVE".islower())   # Outputs FALSE

print("SAVE".isupper())  # Outputs TRUE

print("Boolean".startswith("B"))  # Outputs TRUE
