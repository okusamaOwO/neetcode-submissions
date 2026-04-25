# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # một cái cây sẽ được gọi là valid khi nào?
        if not root:
            return True
        if not root.left and not root.right:
            return True
        inorder_travel = self.inorderTraversal(root)
        # print(inorder_travel)
        s = set()
        for element in inorder_travel:
            s.add(element)
        if inorder_travel == sorted(inorder_travel) and len(s) == len(inorder_travel):
            return True
        return False