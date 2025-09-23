def get_season(m):
    seasons = ("winter","spring","summer","autumn")
    return seasons[(m%12)//3]

month = int(input("Enter month number (1-12): "))
if 1 <= month <= 12:
    print("Season:", get_season(month))
else:
    print("Invalid month")