class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

def main():
    new_car = Car("TLS-22", 179)

    print(f"Registration Number: {new_car.registration_number}")
    print(f"Maximum Speed: {new_car.max_speed} km/h")
    print(f"Current Speed: {new_car.current_speed} km/h")
    print(f"Travelled Distance: {new_car.travelled_distance} km")
    print()

    # accelerate to max speed
    new_car.accelerate(1000)   # big number to guarantee hitting max
    print(f"Current speed after acceleration: {new_car.current_speed} km/h")

    # emergency brake
    new_car.accelerate(-1000)
    print(f"Speed after emergency brake: {new_car.current_speed} km/h")

if __name__ == "__main__":
    main()
