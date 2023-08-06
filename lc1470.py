class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final = []
        s1 = s2 = 0
        s = len(nums)/2
        one = nums[: int(s)]
        two = nums[int(s):]


        while s1 < len(one) and s2 < len(two):
            final.append(one[s1])
            final.append(two[s2])
            s1 +=1
            s2+=1
        while (s1 <len(one)):
            final.append(one[s1])
            s1 +=1
        while (s2 <len(two)):
            final.append(two[s2])
            s2+=1
        return final



