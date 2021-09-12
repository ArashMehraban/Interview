class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [float('inf') for _ in range(amount+1)]
        mem[0] = 0
        
        for i in range(len(mem)):
            for c in coins:
                if i-c >= 0:
                    mem[i] = min(mem[i],mem[i-c]+1)
                    
        if mem[-1] == float('inf'):
            return -1
        else:
            return mem[-1]
        
