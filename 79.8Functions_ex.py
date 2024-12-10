def process_number(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return f"Total: {total}, Average: {round(average, 2)} Min: {minimum}, Max: {maximum}"

result = process_number([1, 2, 3, 4, 5])
print(result)

float_result = process_number([1.5, 2.7, 3.2, 4.9, 5.1])
print(float_result)