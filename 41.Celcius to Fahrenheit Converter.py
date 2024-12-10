# Celcius to Fahrenheit Converter with extra examples
# This script converts a temperature from Celsius to Fahrenheit and demonstrate
# Author:
# Date:
# Rev.:

days_in_week = 7
celsius_temp = 25.0  # Temperature to convert
pi = 3.14159  # Example of a float constant

greetings = "Hello, "
user_name = "Python learner"

is_summer = True

month = ["January", "February", "March"]
temp_scales = {"Celsius":"oC", "Fahrenheit":"oF"}

celsius_to_fahrenheit_factor = 9/5
fahrenheit_offset = 32
fahrenheit_temp = (celsius_temp * celsius_to_fahrenheit_factor) + fahrenheit_offset
fahrenheit_temp = round(fahrenheit_temp,1)

full_greeting = greetings + user_name  # String concatenation

shouted_greeting = full_greeting.upper()  # Convert to uppercase
whispered_greeting = full_greeting.lower()  # Conver to lowercase

month_count = len(month)  # Get length of a string or list

output1 = str(celsius_temp) + temp_scales["Celsius"] + "is equal to" + str(fahrenheit_temp) + temp_scales["Fahrenheit"]

output2 = (f"{celsius_temp}-{temp_scales['Celsius']} is equal to {fahrenheit_temp}-{temp_scales['Fahrenheit']}")

print(full_greeting)
print(shouted_greeting)
print(whispered_greeting)
print(f"Number of months in the list: {month_count}")
print(output1)
print(output2)
print(f"Is this summer? {is_summer}")
print(f"There are {days_in_week}  days in week, and pi is approimately {pi:.2f}")
