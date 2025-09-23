def remove_odds(nums):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    return evens

original = [1, 2, 3, 4, 5, 6]
filtered = remove_odds(original)
print("Original:", original)
print("Without odds:", filtered)