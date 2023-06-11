class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        for i in range(n):
            # find the first non-'a' character
            if s[i] != 'a':
                j = i + 1
                # keep moving forward until 'a' character appears
                while j < n and s[j] != 'a':
                    j += 1
                # perform the operation on the selected substring
                return s[:i] + ''.join(chr(ord(c) - 1) for c in s[i:j]) + s[j:]
        
        # If we reached here, the string is all 'a', replace last 'a' with 'z'
        return s[:-1] + 'z'
