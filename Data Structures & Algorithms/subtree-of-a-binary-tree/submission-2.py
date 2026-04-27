# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.dtraverse(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def dtraverse(self, first, second):
        if not first and not second:
            return True
        if not first or not second:
            return False
        if first.val != second.val:
            return False
        return self.dtraverse(first.left, second.left) and self.dtraverse(first.right, second.right)