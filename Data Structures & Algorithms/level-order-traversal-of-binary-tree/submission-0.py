# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = collections.deque()
        q.append(root)
        # lưu cái đấy kiểu gì được nhỉ hmm im thinking 

        while q:
            level = []
            leng_of_q = len(q)
            for i in range(leng_of_q):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            if level:
                result.append(level)

        return result