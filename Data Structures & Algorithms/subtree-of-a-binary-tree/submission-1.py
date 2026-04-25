# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p:
                return False
            if not q:
                return False
            if p.val == q.val and isSameTree(p.right, q.right) and isSameTree(p.left, q.left):
                return True
            return False
        if not subRoot: # which means subRoot is None? 
            return True
        if not root:
            return False
        # k co cai nao false ca
        if isSameTree(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        return False
