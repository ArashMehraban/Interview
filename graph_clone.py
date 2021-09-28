"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeMap = {}
        
        def dfs(node, nodeMap):
            if node == None:
                return None
            if node.val in nodeMap:
                return nodeMap[node.val]
            newNode = Node(node.val)
            nodeMap[node.val] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor, nodeMap))
            return newNode
        
        return dfs(node, nodeMap)
            
