import collections
class Solution(object):
    def characterReplacement(self, s, k):
        maxlen = 0
        largestCount = 0
        arr = collections.Counter()
        s = input("string: ")
        k = int(input("K value: "))
        
        for idx in range(len(s)):
            arr[s[idx]] += 1
            largestCount = max(largestCount, arr[s[idx]])
            if maxlen - largestCount >= k:
                arr[s[idx - maxlen]] -= 1
            else:
                maxlen += 1
        return maxlen
solution = Solution()
result = solution.characterReplacement("", 0)
print("Max length :", result)
