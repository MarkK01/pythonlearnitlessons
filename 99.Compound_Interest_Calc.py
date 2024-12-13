# Program: Compund Interest Calculator

# Input principal, rate, time, and compounding frequency from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Convert rate to decimal
rate_decimal = rate / 100

# Calculate compound interest
compound_interest = principal * (1 + rate_decimal / n) ** (n * time) - principal

# Calculate the total amount
total_amount = principal + compound_interest

# Print the results
print("\n Compound Interest Calculation:")
print("Principal: $", principal)
print("Annual Interest Rate: ", rate, "%")
print("Time Period: ", time, "years")
print("Compounding Frequency: ", n, "times per year")
print("Compund Interest: $", round(compound_interest, 2))
print("Total Amount: $", round(total_amount,2))
