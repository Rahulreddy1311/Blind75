# Input numbers from the user as a list of integers
nums = [int(x) for x in input("Enter numbers: ").split()]
contains_duplicate = False
n = len(nums)
i = 0
while not contains_duplicate and i < n - 1:
    j = i + 1
    while not contains_duplicate and j < n:
        if nums[i] == nums[j]:
            contains_duplicate = True
        j += 1
    i += 1
if contains_duplicate:
    print("True")
else:
    print("False")
