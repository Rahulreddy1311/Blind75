class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hash_set = {}
        max_len = 0
        r = 0  
        while r < len(s):
            if s[r] in hash_set:
                if hash_set[s[r]] + 1 > l:
                    l = hash_set[s[r]] + 1
            hash_set[s[r]] = r
            max_len = max(max_len, r - l + 1)
            r += 1  

        return max_len

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    solution = Solution()
    result = solution.lengthOfLongestSubstring(input_string)
    print("Length :", result)
