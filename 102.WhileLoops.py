# While Loops

# writing your first while loop
health = 10
while health > 10:
    print(health)
    health -= 1   # forgetting this line will result in infinite loop

# using two or more Loops together is called a nested loop
for i in range(2):  # Outside Loop
    for j in range(3):  # Inside Loop
        print(i, j)