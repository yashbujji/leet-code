class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        values_counter = Counter(nums)
        listed = list(values_counter.values())

        for i in range(len(listed)):
            if listed[i]%2 != 0:
                return False
        return True


