# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            mini_res = []
            len_level = len(queue)
            for i in range(len_level):
                curr = queue.popleft()
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    mini_res.append(curr.val)
            if mini_res:
                res.append(mini_res)
        return res
            

        