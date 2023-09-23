class Solution(object):
    def __init__(self):
        self.num = input("num")
        self.num = list(map(int, self.num.split()))
        self.target = int(input("Target: "))

    def twosum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

sol = Solution()
result = sol.twosum(sol.num, sol.target)
print(result)