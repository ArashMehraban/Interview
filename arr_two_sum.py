class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compDict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in compDict:
                return i,compDict[diff]
            else:
                compDict[nums[i]] = i
        
