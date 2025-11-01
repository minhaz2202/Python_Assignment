class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
        print(f"Elevator starts at floor {self.current}")

    def up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Moved up to floor {self.current}")
        else:
            print("At top floor")

    def down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Moved down to floor {self.current}")
        else:
            print("At bottom floor")

    def go(self, floor):
        print(f"Going to floor {floor}")
        while self.current < floor:
            self.up()
        while self.current > floor:
            self.down()
        print(f"Arrived at floor {self.current}")

#main program
e = Elevator(1, 5)
e.go(3)
e.go(1)
