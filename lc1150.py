class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if nums.count(target) > len(nums) /2:
            return True
        return False
