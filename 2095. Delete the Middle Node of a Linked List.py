# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next== None:
            return None
            
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head
-----------------------------------------------------------------------------------
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:

        if not head.next: return None                   # If only head, then it's the middle node

        ptr1, ptr2 = head.next, head                                       

        while ptr1.next and ptr1.next.next:             # On each iteration, ptr1 jumps two nodes and ptr2
            ptr1 = ptr1.next.next                       # jumps one node, so when ptr1 hits the end of the
            ptr2 = ptr2.next                            # list, ptr1 will be at the middle node.
      
        ptr2.next = ptr2.next.next                      # middle node is removed.

        return head
-----------------------------------------------------------------------------------------
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        if not head or not head.next:
            return None
        
        if not head.next.next:
            head.next = None
            return head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
        slow.val = slow.next.val
        slow.next = slow.next.next
        
        
        return head
