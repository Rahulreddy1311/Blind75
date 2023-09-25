import collections
class Solution(object):
    def characterReplacement(self, s, k):
        maxlen = 0
        largestCount = 0
        arr = collections.Counter()
        
        while True:
            s = input("string: ")
            if s.lower() == 'exit':
                break
            k = int(input("K Value: "))
            
            for idx in range(len(s)):
                arr[s[idx]] += 1
                largestCount = max(largestCount, arr[s[idx]])
                if maxlen - largestCount >= k:
                    arr[s[idx - maxlen]] -= 1
                else:
                    maxlen += 1
            print("Max length:", maxlen)
solution = Solution()
while True:
    solution.characterReplacement("", 0)
