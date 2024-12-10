# Calculate 3 to the power of 4, then find the remainder when divided by 5
results_power = 3 ** 4
print(results_power)
results_expo = results_power % 5
print(results_expo)
results_total = (3 ** 4) % 5
print(results_total)


# 1. Extract the last digit of the encoded message.
# 2. Use this to determine the correspond letter
# 3. Report back with decoded letter.

encoded_message = 1233248916372176407

# Revealing the last letter
last_digit = encoded_message % 26
print(last_digit)

# Converting the digit to a letter (A=0, B=1, C=2)
decoded_letter = chr(last_digit + 65) 

print(f"The last letter of the secret message is: {decoded_letter}")