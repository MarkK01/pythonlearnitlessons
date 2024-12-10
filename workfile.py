from datetime import datetime

# current_year = 2024
current_year = datetime.now().year

age = input("How old are you? ")
birth_year = current_year - int(age)
print("Wow!  You were born in", birth_year)