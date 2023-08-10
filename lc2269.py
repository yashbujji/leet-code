class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        c = 0
        s = str(num)
        for i in range(len(s) - k+1):
            window = int(s[i:i+k])
            if window == 0:
                continue
            if num%window == 0:
                c+=1
        return c 