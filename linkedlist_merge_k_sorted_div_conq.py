# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortTwo(self,l1,l2):
            if not l1: return l2
            if not l2: return l1
            
            dummy = ListNode()
            if l1.val <= l2.val:
                dummy = l1
                dummy.next = self.sortTwo(l1.next,l2)
            else:
                dummy = l2
                dummy.next = self.sortTwo(l1,l2.next)
            return dummy
        
    def div_conq(self,lists,left,right):
            if left == right: return lists[left]
            
            mid  = (left + right)//2
            leftList = self.div_conq(lists, left, mid)
            rightList = self.div_conq(lists,mid+1, right)
            return self.sortTwo(leftList,rightList)
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #using divide and conquer        
        if len(lists) == 0:
            return None
        return self.div_conq(lists,0,len(lists)-1)
       
