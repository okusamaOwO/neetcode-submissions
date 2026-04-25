# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visisted = {}
        while head is not None:
            if head not in visisted:
                visisted[head] = 0
                head = head.next
            else:
                return True 
        return False 