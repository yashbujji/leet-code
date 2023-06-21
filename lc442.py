class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        if len(nums) ==1:
            return []

        for i in range(1,len(nums)) :
            if nums[i] == nums[i-1] and (len(arr) == 0 or nums[i] != arr[-1]):
                arr.append(nums[i])
        return arr


    