# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        largest = float('-inf')
        return self.traverse(root, largest)
        
    def traverse(self, root: TreeNode, path_max):
        if root:

            if root.val >= path_max:
                return 1 + self.traverse(root.left, root.val) + self.traverse(root.right, root.val)
            else:
                return self.traverse(root.left, path_max) + self.traverse(root.right, path_max)
        else:
            return 0      
