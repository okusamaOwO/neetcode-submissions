# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # p và q là cái subtree của cái root đó? ừ
        if not root:
            return False
        current_ancestor = root
        while p.val < current_ancestor.val and q.val < current_ancestor.val :
            current_ancestor = current_ancestor.left
        while p.val > current_ancestor.val and q.val > current_ancestor.val :
            current_ancestor = current_ancestor.right
        return current_ancestor    
        