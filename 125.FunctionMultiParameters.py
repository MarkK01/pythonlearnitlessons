# Functions with Multiple Parameters

def make_schedule(period1, period2):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title())
    return schedule

student_schedule = make_schedule("math", "history")
print("SCHEDULE:", student_schedule)

def format_info(name, age, school):
    return("Student: " + name + "\nAge: " + str(age) + "\nSchool: " + school)
print(format_info("Tobias Ledford", 15, "Oak"))

# Sequence

first_name = "Vitalii"

def hat_available(color):
    hat_colors = "black, red, blue, green, white, grey, brown, pink"
    return(color.lower() in hat_colors)

have_hat = hat_available("green")
print("hat available is", have_hat)   # Output: hav available is True
