nums = input("Enter numbers separated by spaces: ").split()
unique_nums = set()
contains_duplicate = False
for num in nums:
    if num in unique_nums:
        contains_duplicate = True
        break
    unique_nums.add(num)
if contains_duplicate:
    print("True")
else:
    print("False")
