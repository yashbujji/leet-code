class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count =0
        arr = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
            i = i+1
        return arr
