# Savings Calculator Starter File

# Task 1: Setting Up Variables
# Create variables for monthly savings here
month1 = 200.50
month2 = 157.25
month3 = 250.25
month4 = 300.75

# Task 2: Calculating Total Savings
# Calculate total savings here
total_savings = month1 + month2 + month3 + month4

# Task 3: Calculating Average Savings
# Calculate average savings here
num_month = 4
average_savings = total_savings / num_month

# Task 4: Formatting and Printing Results
# Print the formatted results here
print(f"Total savings over {num_month} months: ${total_savings:.2f}")
print(f"Average monthly savings: ${average_savings:.2f}")

# Bonus Challenges:
# 1. Modify the program to handle 4 months of savings
# 2. Round the average savings to the nearest whole dollar
# 3. Calculate what percentage each month's savings contribute to the total

# Bonus Code here
# 2. Round the average savings to the nearest whole dollar
rounded_average = round(average_savings)
print(f"Rounded average monthly savings: ${rounded_average}")