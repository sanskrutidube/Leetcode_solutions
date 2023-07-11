# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. Find middle node
        # 2. Reverse a LL
        # 3. Merge two sorted lists

        # step 1:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, curr = None, slow.next
        slow.next = None

        # step 2:
        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        # step 3:
        dummy = curr = ListNode(0)

        head1, head2 = head, prev

        while head1 and head2:
            if head1:
                curr.next, head1 = head1, head1.next
                curr = curr.next
            if head2:
                curr.next, head2 = head2, head2.next
                curr = curr.next

        curr.next = head1 or head2
