# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], L: int, R: int) -> int:
        res = []
        self.inorder(root, res, L, R)
        return sum(res)

    def inorder(self, root, res, L, R):
        cur = root
        if not cur:
            return None
        self.inorder(cur.left, res, L, R)
        if L <= cur.val <= R:
            res.append(cur.val)
        self.inorder(cur.right, res, L, R)