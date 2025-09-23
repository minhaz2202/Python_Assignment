import math

def unit_price(diameter_cm, price_eur):
    radius_m = diameter_cm / 100 / 2
    area = math.pi * radius_m * radius_m
    return price_eur / area

diam1 = float(input("Diameter of first pizza (cm): "))
price1 = float(input("Price of first pizza (eur): "))
diam2 = float(input("Diameter of second pizza (cm): "))
price2 = float(input("Price of second pizza (eur): "))

unit1 = unit_price(diam1, price1)
unit2 = unit_price(diam2, price2)

print("Unit price pizza 1: €", unit1, "per m2")
print("Unit price pizza 2: €", unit2, "per m2")

if unit1 < unit2:
    print("First pizza is better value for money.")

else:
    print("Second pizza is better value for money.")