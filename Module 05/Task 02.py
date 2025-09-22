numbers = []
while True:
    user = input("Enter a number (or press enter to quit): ")
    if user == "":
        break
    numbers.append(int(user))

numbers.sort(reverse=True)
print("The five greatest numbers are:", numbers[:5])