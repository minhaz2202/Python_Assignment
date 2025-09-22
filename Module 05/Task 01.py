import random

num = int(input("How many dice? "))
sum = 0

for i in range(num):
    sum += random.randint(1,6)

print("sum of rolls is:", sum)