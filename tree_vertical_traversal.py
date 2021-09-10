# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        Map = defaultdict(list)
        def dfs(r,c,node):
            if not node:
                return
            dfs(r-1,c+1,node.left)
            dfs(r+1,c+1,node.right)
            Map[(r,c)].append(node.val)
        
        dfs(0,0,root)
        output= []
        old = float('-inf')
        for k,v in sorted(Map.items()):
            if k[0] != old:
                output.append([])
            output[-1].extend(sorted(v))
            old = k[0]
        return output
        
