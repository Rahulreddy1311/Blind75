class Solution(object):
    def __init__(self):
        self.num = input("num")
        self.num = list(map(int, self.num.split()))
        self.target = int(input("Target: "))
        

    def twosum(self, num, target):
        n = len(num)
        for i in range(n):
            for j in range(i + 1, n):
                if num[i] + num[j] == target:
                    return [i, j]
        return [] 

sol = Solution()
result = sol.twosum(sol.num, sol.target)
print(result)