# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 1
        self.kth = None
        
        def inorder(node):
            if not node or self.kth:
                return
            
            inorder(node.left)
            if self.count == k:
                self.kth = node.val
            self.count +=1
            inorder(node.right)
            
        inorder(root)
        return self.kth
        
