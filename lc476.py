class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:]
        m = ''
        for i in s:
            if i == '1':
                m += '0'
            else:
                m += '1'
        return int(m,2)





