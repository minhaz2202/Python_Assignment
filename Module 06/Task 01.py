import random

def roll_dice():
    """Return a random integer between 1 and 6 (inclusive)."""
    return random.randint(1, 6)

def main():
    result = None
    while result != 6:
        result = roll_dice()
        print("Rolled:", result)

if __name__ == "__main__":
    main()
