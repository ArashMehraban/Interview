class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for a in range(len(nums)-1):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a-1]:
                continue
            l,r = a+1, len(nums) -1
            while(l<r):
                if nums[a] + nums[l] + nums[r] < 0:
                    l+=1
                elif nums[a] + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    output.append([nums[a],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return output
        
        
