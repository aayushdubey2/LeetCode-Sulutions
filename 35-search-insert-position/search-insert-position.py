class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if target-nums[i] == 0: 
                return i
            elif target-nums[i] > 0:
                continue
            else: 
                return i
        return len(nums) 
        