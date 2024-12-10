# 1. Grocery Budget Calculator
# TODO: Calculate monthly grocery expenses
# Hint: Use float() for input and multiply weekly by 4

# weekly_groceries = float(input("Enter Weekly Grocery Spending: "))
# monthly_expenses = weekly_groceries * 4

# print(f"Monthly expenses are: ${monthly_expenses:,.2f}")

# 2. Temperature Converter
# TODO: Convert Celcius to Fahrenheit
# Hint: Formula is (C * 9/5) + 32

# celcius_temp = float(input("What is temperature in Celcius: "))
# fahrenheit_temp = (celcius_temp * 9 / 5) + 32
# print(f"Celcius {celcius_temp} temperature converted to Fahrenheit is: {fahrenheit_temp:.1f}")

# 3. Tip Calculator
# Calculate tip amount based on bill and percentage
# HINT: bill amount * (tip percentage / 100)

# bill_amount = float(input("Enter bill amount: $"))
# tip_percentage = float(input("Enter tip percentage: %"))

# tip_amount = bill_amount * (tip_percentage / 100)
# print(f"The tip amount on bill of $ {bill_amount:,.2f} with tip percentage {tip_percentage:.2f} is ${tip_amount:,.2f}")

# 4. Savings Goal Tracker
# TODO: Calculate months to reach the savings
# Hint: Divide gloal by monthly savings

# savings_goal = float(input("Enter your savings goal: $"))
# monthly_savings = float(input("Enter your monthly savings: $"))
# months_to_goal = savings_goal / monthly_savings
# print(f"It will take {months_to_goal} months to reach your goal")

# 5. Paint Calculator
# TODO: Calculate gallons of paint needed
# Hint: Divide total wall area by paint coverage per gallon. Use 'math'
# module.  'math.ceil()' rounds up to the nearest integer
# 'math.floor()' rounds down to the nearest integer
# 'round()' rounds to the nearest integer (0.5 rouns up to 1)

# wall_area = float(input("Enter the total wall area in square feet: "))
# paint_coverage = float(input("Enter the paint coverage per gallon: "))
# paint_needed = wall_area / paint_coverage
# print(f"You need {paint_needed} gallons of paint")

# import math #Import the math modeule for advanced mathematical operation

# wall_area = float(input("Enter the total wall area in square feet: "))
# paint_coverage = float(input("Enter the paint coverage per gallon: "))
# paint_needed = wall_area / paint_coverage

# # Different rounding methods
# # math.ceil() rounds up to the nearest integer
# ceil_round = math.ceil(paint_needed)

# # math.floor() rounds down to the nearest integer
# floor_round = math.floor(paint_needed)

# # round() rounds to the nearest integer (0.5 rouns up to 1)
# normal_round = round(paint_needed)

# # Custom rounding to the nearest half gallon
# # Multiply by 2, round to the nearest integer, then divide by 2
# round_to_half = round(paint_needed * 2) / 2

# # Print the results
# # The :.2f format specifier shows 2 decimal places for float values
# print(f"Exact month: {paint_needed:.2f} gallons of paint.")
# print(f"Rounded up (celing):{ceil_round} gallon(s).")
# print(f"Rounded down (flow):{floor_round} gallon(s).")
# print(f"Normal round:{normal_round} gallon(s).")
# print(f"Rounded to nearest half gallon:{round_to_half:.1f} gallons(s).")

# 6. Fuel Efficiency Calculator
# TODO: Calculate miles per gallon
# Hint: Divide miles driven by gallons used
# miles_driven = float(input("Enter miles driven: "))
# gallons_used = float(input("Enter gallons used: "))
# miles_per_gallon = miles_driven / gallons_used
# print(f"Miles driven {miles_driven} and gallons used {gallons_used} results in {miles_per_gallon} miles per gallon. ")

# 7. BMI Calculator
# TODO: Calculate Body Mass Index (BMI)
# Hint: formula is BMI = weight(kg) / (height(m)**2)
# weight_kg = float(input("Enter your weight in kilograms: "))
# height_m = float(input('Enter your height in meters: '))
# bmi = weight_kg / (height_m ** 2)
# print(f"Your BMI is {bmi}")

# # 8. Currency Converter
# # TODO: Convert USD to EUR
# # Hint: Multiple USD amount by exchange rate
# usd_amount = float(input("Enter US Dollars amount: "))
# exchange_rate = float(input("Enter exchange USD to EUR exchange rate: "))
# eur_amount = usd_amount * exchange_rate
# print(f"EUD Dollars is: {eur_amount}")

# 9. Mortgage Payment Calculator
# TODO: Calculate monthly mortgage payment
# Hint: Use the formula:  P * (r(1+r)^n / ((1+r)^r - 1))
# where P = principal, r = monthly rate, n = number of payments
loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (%): "))
loan_term_years = float(input("Enter the loan term in years: "))
monthly_payments = (loan_amount * (annual_interest_rate / 1200)) / (1 - (1 + annual_interest_rate / 1200) ** (-loan_term_years * 12))
print(f"Your monthly mortgage payment is ${monthly_payments}")
