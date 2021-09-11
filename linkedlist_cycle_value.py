# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Floyd's tortoise and hare
        # slow :  tortoise 
        # fast :  hare
        
        if not head or not head.next:
            return None
        
        slow = fast = entry = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow==fast:
                while slow!=entry:
                    entry = entry.next
                    slow = slow.next
                return entry
            
        return None

            

        
            
        
        
        
        
