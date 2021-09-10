"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # No hash table. Use interweaving:
        # Old List: A --> B --> C --> D
        # InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
        dummy = Node(-1)
        dummy.next = head
        cur = head 
        
        #interweave:
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        cur = head
        
        # update random ptrs
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        #remove old list nodes
        cur = dummy
        old = head
        while old:
            cur.next = old.next
            cur = old
            old = cur.next
        return dummy.next
