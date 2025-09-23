airports = {}

while True:
    choice = input("\n1. Add Airport\n2. Get Airport Info\n3. Quit\nChoose an option: ").strip()

    if choice == '1':
        icao = input("Enter ICAO code: ").strip().upper()
        name = input("Enter airport name: ").strip()
        airports[icao] = name
        print(f"Added: {icao} - {name}")

    elif choice == '2':
        icao = input("Enter ICAO code: ").strip().upper()
        print(f"{icao}: {airports.get(icao, 'Not found')}")

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")