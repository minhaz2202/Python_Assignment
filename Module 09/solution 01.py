class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def status(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")

def main():
    new_car = Car("TLS-22", 179)
    print("Car Properties:")
    new_car.status()

if __name__ == "__main__":
    main()
