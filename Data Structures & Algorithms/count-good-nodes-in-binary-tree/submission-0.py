# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 3 1 2 1 1 5
        s = []
        def inorder(root, max):
            if not root:
                return []
            if root.val >= max:
                max = root.val
                s.append(root.val)
            return inorder(root.left, max) + [root.val] + inorder(root.right, max)
        max = root.val
        inorder(root, max)
        return len(s)

            
