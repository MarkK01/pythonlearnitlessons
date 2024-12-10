# Split The Bill Program

# Step 1: Set up our variable
total_bill = 128
number_of_friends = 5

# Step 2: Calculate the individual share
individual_share = total_bill / number_of_friends


# Bonus challenge
# 1. Include a 15% tip in the total bill before splitting.
# 2. Round the indvidual share to two decimal places (hint: look up the round() function)

# 1. Include a 15% tip in the total bill before splitting.
tip_percentage = 0.15
tip_amount = total_bill * tip_percentage
total_with_tip = total_bill + tip_amount

# 2. Round the indvidual share to two decimal places (hint: look up the round() function)
rounded_share = round(individual_share, 2)

# Step 3: Display the results
print(f"Original bill: ${total_bill}")
print(f"Tip amount (15%): ${tip_amount}")
print(f"Total bill with tip: ${total_with_tip}")
print(f"Number of friends: {number_of_friends}")
print(f"Each person should pay: ${rounded_share}")
