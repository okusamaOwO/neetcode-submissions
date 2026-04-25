# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # nếu head is None or head.next equal to None -> return False
        if head is None or head.next is None:
            return False
        # what's else
        slow_pointer = head
        fast_pointer = head.next
        
        # xử lí đoạn fast_poiner như nào? 
        while slow_pointer is not None:
            slow_pointer = slow_pointer.next
            if fast_pointer.next is None:
                return False
            if fast_pointer.next.next is None:
                return False
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False
