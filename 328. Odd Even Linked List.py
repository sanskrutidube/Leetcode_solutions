class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        slow,fast = head,head.next
        cur=h1=head.next
        while fast:
            if fast.next:
                slow.next = fast.next
                slow = slow.next
                fast=fast.next.next
            else:
                break
            cur.next=fast
            cur = cur.next
        slow.next = h1
        return head
