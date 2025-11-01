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


#main program
def main():
    # Elevator spans floors 1 to 10
    e = Elevator(1, 10)
    e.move_to(5)
    e.move_to(1)

if __name__ == "__main__":
    main()
