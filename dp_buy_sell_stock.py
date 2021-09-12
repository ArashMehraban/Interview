class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curmax, globalmax = 0,0
        
        for i in range(1,len(prices)):
            curmax = max(curmax+prices[i]-prices[i-1],0)
            globalmax = max(globalmax,curmax)
        
        return globalmax
        
