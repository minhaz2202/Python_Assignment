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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace status: {self.name}")
        print(f"{'Car':<12}{'MaxSpeed':<10}{'CurrSpeed':<10}{'Distance'}")
        for car in self.cars:
            print(f"{car.registration_number:<12}{car.max_speed:<10}"
                  f"{car.current_speed:<10}{car.travelled_distance:.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

def main():
    cars = []
    for i in range(1, 6):
        cars.append(Car(f"CAR-{i}", random.randint(100, 200)))

    race = Race("Halloween Race", 1000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 5 == 0:
            print(f"\n--- Hour {hours} ---")
            race.print_status()

    print(f"\nThe race '{race.name}' finished after {hours} hours!")
    race.print_status()

if __name__ == "__main__":
    main()