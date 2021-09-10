# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        import sys
        def validate(root,Min=-sys.maxsize,Max=sys.maxsize):
            if root == None:
                return True
            if root.val > Min and root.val < Max and validate(root.left,Min,root.val) and validate(root.right,root.val,Max):
                return True
            else:
                return False
            
        return validate(root,-sys.maxsize,sys.maxsize)
            
        
