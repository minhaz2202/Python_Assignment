def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

# test
my_list = [2, 5, 8, -3, 10]
print("Sum:", sum_list(my_list))