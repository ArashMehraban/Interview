class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        N = len(s)
        
        mem = [False for _ in range(N+1)]
        mem[0] = True
        for begin in range(N):
            if not mem[begin]: continue
            for end in range(begin+1,N+1):
                if s[begin:end] in d:
                    mem[end] = True
        
        return mem[-1]
        
