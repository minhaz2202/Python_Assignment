while True:
    inches = float(input("Enter the inches (negative to quit): "))
    if inches < 0:
        break
    cm = inches * 2.54
    print(f"{inches} inches = {cm:.2f} cm")