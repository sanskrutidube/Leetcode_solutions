# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start= ListNode()
        start.next=head
        fast= start
        slow= start
        for i in range(1,n+1):
            fast=fast.next
        while fast.next!= None:
            fast= fast.next
            slow=slow.next
        slow.next = slow.next.next
        return start.next
-----------------------------------------------------
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def index(node):
            if not node:
                return 0
            i = index(node.next)+1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next
