# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getHeight(node): # khoảng cách tới root 
            if node is None:
                return -1
            if node.left is None and node.right is None:
                return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1
        print(getHeight(root))
        if root.right is None and root.left is None:
            return 0
        if root.right is not None and root.left is not None: 
            return getHeight(root.right) + getHeight(root.left) + 2
        if root.left is None:
            # có con bên phải
            print("k co con trai")
            return max(getHeight(root), self.diameterOfBinaryTree(root.right))
        if root.right is None:
            print("k co con phai")
            return max(getHeight(root), self.diameterOfBinaryTree(root.left))

        
