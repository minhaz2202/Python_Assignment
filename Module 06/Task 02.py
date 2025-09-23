import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("How many sides does the dice have? : "))
    target = sides
    roll = None
    while roll != target:
        roll = roll_dice(sides)
        print("Rolled:", roll)
    print("Rolled the maximum (", target, "), done!")

if __name__ == "__main__":
    main()