class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m,n = len(forest), len(forest[0])
        heap = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(heap,(forest[i][j],i,j))
                    
        i,j = 0,0
        res = 0
        while heap:
            _, destx, desty = heapq.heappop(heap)
            step = self.bfs(forest,i,j,destx,desty)
            if step < 0:
                return -1
            res += step
            i,j = destx,desty
        return res
    
    def bfs(self,forest,i,j,destx,desty):
        m,n = len(forest), len(forest[0])
        q = collections.deque()
        q.append([i,j])
        visited = set()
        visited.add((i,j))
        step = 0
        
        while q:
            sz = len(q)
            for _ in range(sz):
                i,j = q.popleft()
                if i == destx and j == desty:
                    return step
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    x = i+dx
                    y = j+dy
                    
                    if (x < 0 or
                        y < 0 or 
                        x >= m or
                        y >= n or
                        (x,y) in visited or
                        forest[x][y] == 0):
                        continue
                    q.append([x,y])
                    visited.add((x,y))
            step += 1
        return -1
