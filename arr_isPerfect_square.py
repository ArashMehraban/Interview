class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 0, num
        while l <= r:
            mid = (l+r)//2
            sqrd = mid * mid
            if num == sqrd:
                return True
            elif num > sqrd:
                l = mid + 1
            else:
                r = mid -1
                
        return False
        
