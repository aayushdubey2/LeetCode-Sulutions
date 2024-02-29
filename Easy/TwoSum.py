# O(n2) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                    

# Solution using hashmap
# Create a hasmap to store the indexes of the numbers in the array
# using enumerate to get the indexes

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap= {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in numMap:
                return [numMap[difference],i]
            numMap[num]=i
