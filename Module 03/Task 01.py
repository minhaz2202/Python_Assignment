#zander size limit check
zander_length = int(input("Enter the length of the zander in cm: "))

if zander_length >= 42:
    print("You may keep the fish.")
else:
    difference = 42 - zander_length
    print(f"Release the fish back into the lake. It is {difference} cm below the size limit.")