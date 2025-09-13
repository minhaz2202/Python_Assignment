numbers = []
while True:
    s = input("Enter a number (empty to quit): ")
    if s == "":
        break
    numbers.append(float(s))

if numbers:  # only print if we have at least one number
    print("smallest:", min(numbers))
    print("largest:", max(numbers))
else:
    print("no numbers entered.")