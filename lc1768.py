class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1 = 0
        s2 = 0
        ans = ""

        while (s1<len(word1) and (s2<len(word2))):
            ans += word1[s1]
            ans += word2[s2]
            s1 +=1
            s2 += 1
        while (s1 < len(word1)):
            ans += word1[s1]
            s1 += 1
        while (s2 < len(word2)):
            ans += word2[s2]
            s2 += 1
        return ans



        



