class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k ==0:
            return 0
        char_count = {}
        max_length = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in char_count:
                char_count[s[r]]=1
            else:
                char_count[s[r]] += 1       
            while len(char_count) >k:
                char_count[s[l]] -= 1
                if char_count[s[l]] ==0:
                    del char_count[s[l]]
                l +=1        
            max_length = max(max_length, r-l+1)
        return max_length
