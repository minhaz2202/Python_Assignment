class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
        print(f"Elevator starts at floor {self.current}")

    def move_to(self, floor):
        if floor < self.bottom or floor > self.top:
            print("Invalid floor")
            return
        print(f"Moving to floor {floor}")
        self.current = floor
        print(f"Elevator arrived at floor {self.current}")


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]
        print(f"Building has {num_elevators} elevators.")

    def use_elevator(self, num, floor):
        if num < 1 or num > len(self.elevators):
            print("Invalid elevator number!")
            return
        self.elevators[num-1].move_to(floor)



#main program
def main():
    building = Building(1, 10, 2)
    building.use_elevator(1, 6)
    building.use_elevator(2, 3)
    building.use_elevator(1, 1)


if __name__ == "__main__":
    main()
