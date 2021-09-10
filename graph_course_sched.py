class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        
        adj = {}
        for item in prerequisites:
            if item[0] not in adj:
                adj[item[0]] = []
            if item[1] not in adj[item[0]]:
                adj[item[0]].append(item[1])
            if item[1] not in adj:
                adj[item[1]] = [] 

        color = {}
        for course in adj:
            color[course] = 'W'
            
        def dfs(course,color):
            color[course] = 'G'
            for pre in adj[course]:
                if color[pre] == 'W':
                    if dfs(pre,color):
                        return True
                elif color[pre] == 'G':
                    return True
            color[course] = 'B'
            return False               
                
        cyc = True
        for course in adj:
            if color[course] == 'W':
                if dfs(course,color):
                    cyc = False
                    break
        return cyc
                
                
                
                        
        
                    
                
                
            
        
        
