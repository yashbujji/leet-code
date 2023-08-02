class Solution:
    def reverseWords(self, s: str) -> str:
        sa = s.split()
        arr =[]
        for i in range(len(sa)):
            val = sa[i][::-1]
            arr.append(val)
        return ' '.join(arr)


        

