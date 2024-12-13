# Program: Simple Interest Calculator

# Input principal, reate, and time from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate(%): "))
time = float(input("Enter the time period (in years): "))

# Caluclate simple interest
simple_interest = (principal * rate * time) / 100

# Calculate the total amount
total_amount = principal + simple_interest

# Print the results
print("\n Simple Interest Calculation:")
print("Principal: $", principal)
print("Annual Interest Rate: ", rate, "%")
print("Time Period: ", time, "years")
print("Simple Interest: $", simple_interest)
print("Total Amount: $", total_amount)
