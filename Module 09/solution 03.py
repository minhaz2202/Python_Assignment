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

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

def main():
    car = Car("TLS-22", 179)

    print(f"Registration Number: {car.registration_number}")
    print(f"Maximum Speed: {car.max_speed} km/h")
    print(f"Current Speed: {car.current_speed} km/h")
    print(f"Travelled Distance: {car.travelled_distance} km")
    print()

    car.accelerate(150)
    print(f"Current speed after acceleration: {car.current_speed} km/h")

    car.accelerate(-200)
    print(f"Speed after emergency brake: {car.current_speed} km/h")

    # Example drive
    car.current_speed = 60
    car.drive(2)
    print(f"Travelled Distance after driving: {car.travelled_distance} km")

if __name__ == "__main__":
    main()
