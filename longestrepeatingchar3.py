import collections
def characterReplacement(s, k):
    maxlen = 0
    largestCount = 0
    arr = collections.Counter()
    for idx in range(len(s)):
        arr[s[idx]] += 1
        largestCount = max(largestCount, arr[s[idx]])
        if maxlen - largestCount >= k:
            arr[s[idx - maxlen]] -= 1
        else:
            maxlen += 1
    return maxlen
s = input("string: ")
k = int(input("K Value: "))
result = characterReplacement(s, k)
print("Max length", result)
