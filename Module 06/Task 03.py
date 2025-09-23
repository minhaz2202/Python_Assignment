def gallons_to_liters(gallons):
    return gallons * 3.78541

while True:
    gallons = float(input("Enter gallons (negative to quit): "))
    if gallons < 0:
        break
    print(gallons_to_liters(gallons), "liters")