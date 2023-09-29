from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
solution = Solution()
nums = [int(x) for x in input("Enter numbers: ").split()]
result = solution.containsDuplicate(nums)
if result:
    print("True")
else:
    print("False")
