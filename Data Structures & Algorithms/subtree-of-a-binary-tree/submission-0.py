# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            if p and not q:
                return False
            if not p and q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        if not subRoot: # neu subroot is none return true 
            return True
        # new subroot is a normal node
        if not root: # neu root lai la none 
            return False
        if isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))