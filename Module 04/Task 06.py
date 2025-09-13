import random

points = int(input("Enter number of random points: "))
inside = 0

for _ in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        inside += 1

pi_estimate = 4 * inside / points
print("Approximation of pi:", pi_estimate)
