# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #use a heap
        hp = []
        
        for i, lst in enumerate(lists):
            if lst: heappush(hp,(lst.val,i))
        
        dummy = cur = ListNode(-1)
        
        while hp:
            val , i = heappop(hp)
            cur.next = ListNode(val)
            if lists[i].next:
                heappush(hp,(lists[i].next.val,i))
                lists[i] = lists[i].next
            cur = cur.next
        return dummy.next
        
