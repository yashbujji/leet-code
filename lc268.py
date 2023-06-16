class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        if nums[-1] != len(nums):
            return len(nums)
        
        elif nums[0] != 0:
            return 0

        for i in range(1,len(nums)):
            exp = nums[i-1]+1

            if nums[i] != exp:
                return exp

