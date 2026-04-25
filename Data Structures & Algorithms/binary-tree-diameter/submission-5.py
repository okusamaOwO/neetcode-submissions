# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getHeight(node): # khoảng cách tới root 
            if not node:
                return 0
            return max(getHeight(node.right), getHeight(node.left)) + 1
        if not root:
            return 0
        left_height = getHeight(root.left)
        right_height = getHeight(root.right)
        diameter = left_height + right_height
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)
