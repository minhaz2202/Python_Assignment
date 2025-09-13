talent = float(input("Enter Talent: "))
pound = float(input("Enter Pound: "))
lot = float(input("Enter lot; "))


talent_pound = 20
pound_lot = 32
lot_gram = 13.3

total_gram = (talent * talent_pound * pound_lot * lot_gram) + (pound * pound_lot * lot_gram) + (lot * lot_gram)

kilograms = int(total_gram //1000)
grams = total_gram % 1000


print("\nThe weight: ")
print(f"{kilograms} kilograms and {grams:.2f} grams. ")