# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        result = []
        queue.append(root)
        while len(queue) != 0:
            # if len(queue) != 0:
            level = []
            for i in range(len(queue)):
                pop_node = queue[0]
                level.append(pop_node.val)
                queue = queue[1:]
                if pop_node.left:
                    queue.append(pop_node.left)
                if pop_node.right:
                    queue.append(pop_node.right)
            result.append(level)
        return result


            