# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # there is a cycle in a linked list if at least one node in the list can be visited again 
        # by following the next pointer 
        if not head:
            return False
        if not head.next:
            return False
        slow_pointer = head
        faster_pointer = head.next 
        # ừ, nghĩa là nếu như mà hai cái pointer này mà gặp được nhau thì ok -> có cycle 
        # else -> không có cycle
        while slow_pointer and faster_pointer:
            if slow_pointer == faster_pointer:
                return True
            if slow_pointer.next: 
                slow_pointer = slow_pointer.next
            else:
                return False
            if not faster_pointer.next:
                return False
            if faster_pointer.next.next:
                faster_pointer = faster_pointer.next.next
            else:
                return False
        return False 
