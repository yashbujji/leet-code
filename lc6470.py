class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return -1
        
        mini = 0
        maxi = 0
        
        if len(nums) > 2:
            mini = min(nums)
            nums.remove(mini)
            maxi = max(nums)
            nums.remove(maxi)
            
        rand = random.choice(nums)
        return rand
            
    
        