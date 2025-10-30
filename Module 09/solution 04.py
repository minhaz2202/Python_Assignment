import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# Main program
cars = [
    Car("TLS-1", random.randint(100, 200)),
    Car("TLS-2", random.randint(100, 200)),
    Car("TLS-3", random.randint(100, 200))
]

for hour in range(1, 4):
    print("Hour", hour)
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        print(car.registration_number, "Speed:", car.current_speed, "Distance:", car.travelled_distance)
    print()

winner = max(cars, key=lambda c: c.travelled_distance)
print("Winner is", winner.registration_number, "with distance", winner.travelled_distance)
