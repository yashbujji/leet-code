class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        maximum = 0
        l = 0
        for r in range(len(s)):
            while len(set(s[l:r+1])) > 2:
                l+=1
            maximum = max(maximum,r-l+1)
        return maximum