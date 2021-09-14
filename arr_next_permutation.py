class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[1,2,5,4,3,2,1]
        #     |       <--- moving pivot to the left
        #    pivot
        pivot = 0
        num_sz = len(nums)
        for i in range(num_sz-1,0,-1): # we  do check the very first elem in nums because of condition below:
            if nums[i-1] < nums[i]:
                pivot = i
                break
        print(pivot)
            
        if pivot == 0:
            nums.sort()
            return
        swap = num_sz-1 # swap index
        while nums[pivot-1] >= nums[swap]:
            swap -=1
        nums[swap], nums[pivot-1] = nums[pivot-1],nums[swap]
        nums[pivot:] = nums[pivot:][::-1] # reverese from nums[pivot:]
        
        
