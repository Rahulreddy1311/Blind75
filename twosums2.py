class Solution(object):
    def __init__(self):
        self.num = input("num")
        self.num = list(map(int, self.num.split()))
        self.target = int(input("Target: "))

    def twosum(self, num, target):
        n = len(num)
        i = 0
        while i < n - 1:
            j = i + 1
            while j < n:
                if num[i] + num[j] == target:
                    return [i, j]
                j += 1
            i += 1
        return []
    
sol = Solution()
result = sol.twosum(sol.num, sol.target)
print(result)