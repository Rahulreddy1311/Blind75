class Solution(object):
    def __init__(self):
        self.num = input("num")
        self.num = list(map(int, self.num.split()))
        self.target = int(input("Target: "))
    
    def twosum(self, num, target):
        dict = {}
        for i in range(len(num)):
            complement = target - num[i]
            if complement in dict:
                return dict[complement], i
            dict[num[i]] = i

sol = Solution()
result = sol.twosum(sol.num, sol.target)
print(result)