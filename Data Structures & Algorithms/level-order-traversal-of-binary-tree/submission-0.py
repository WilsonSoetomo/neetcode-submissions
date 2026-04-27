# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            mini_res = []
            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    mini_res.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if mini_res:
                res.append(mini_res)
        return res

        