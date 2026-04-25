# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        left_tree_result = self.inorderTraversal(root.left)
        result += left_tree_result
        result.append(root.val)
        right_tree_result = self.inorderTraversal(root.right)
        result += right_tree_result
        return result 
            
            
