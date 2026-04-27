# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            qlen = len(q)
            mini_res = []
            for i in range(qlen):
                curr = q.popleft()
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    mini_res.append(curr.val)
            if mini_res:
                res.append(mini_res[-1])
        return res