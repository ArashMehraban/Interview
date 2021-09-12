class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        n = len(nums)
        for i in range(n - 2):
            s = i + 1
            e = n - 1
            while s < e:
                Sum = nums[i] + nums[s] + nums[e]
                if abs(Sum-target) < abs(res-target):
                    res = Sum
                if Sum < target:
                    s += 1
                else:
                    e -= 1
        return res
        
