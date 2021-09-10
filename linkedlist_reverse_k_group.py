# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = dummy =ListNode(0)
        cur = head
        dummy.next = head
        length = 0
        while head:
            length += 1
            head = head.next
            
        for i in range(length // k):
            for j in range(k - 1):
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
            prev = cur
            cur = prev.next
        return dummy.next
