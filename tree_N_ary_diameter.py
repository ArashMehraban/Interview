"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    
    def dfs(self,node):
        if not node:
            return 0
        max1 = 0
        max2 = 0
        for child in node.children:
            nodeDepth = self.dfs(child) +1
            if nodeDepth > max1:
                max1, max2 = nodeDepth, max1
            elif nodeDepth > max2:
                max2 = nodeDepth
        self.diameter = max(self.diameter, max1 + max2)
        return max1 
