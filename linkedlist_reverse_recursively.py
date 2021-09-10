# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursively
        def rec(prev,cur):
            if not cur:
                return prev
            end = rec(cur,cur.next)
            cur.next = prev
            return end
        return rec(None,head)
