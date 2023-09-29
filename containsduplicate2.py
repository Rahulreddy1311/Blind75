nums = [int(x) for x in input("Enter numbers: ").split()]
if len(nums) != len(set(nums)):
    print("True")
else:
    print("False")
