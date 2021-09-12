class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        N  = len(words)
        cost = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(min(len(words[i]), len(words[j])), -1,-1):
                    if words[i][-k:] == words[j][:k]:
                        cost[i][j] = k
                        break
        mem = [[(float('inf'),'')]*N for _ in range(1<<N)]
        for i in range(N):
            mem[1<<i][i] = (len(words[i]),words[i])
            
        for bitmask in range(1<<N):
            bits = [j for j in range(N) if bitmask & (1<<j)]
            for add,src in permutations(bits,2):
                cand = mem[bitmask^(1<<add)][src][1] + words[add][cost[src][add]:]
                mem[bitmask][add] = min(mem[bitmask][add],(len(cand),cand))
        
        return min(mem[-1])[1]
                           
        
