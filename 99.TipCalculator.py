# Program: Tip Calculator

# Input bill amount and tip percentage from the user
bill_amount = float(input("Enter the bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (%): "))

# Calculate the tip amount
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate the total amount (bill + tip)
total_amount = bill_amount + tip_amount

# Print the results
print("\nTip Calculator:")
print("Bill Amount: $", bill_amount)
print("Tip Percentage: ", tip_percentage, "%")
print("Tip Amount: $", round(tip_amount, 2))
print("Total Amount: $", round(total_amount, 2))

# Aske for the number of people splitting the bill
num_people = int(input("\nEnter the number of people splitting the bill: "))

# Calculate the amount per person
amount_per_person = total_amount / num_people

# Print the results
print("Amount per person: $", round(amount_per_person, 2))

