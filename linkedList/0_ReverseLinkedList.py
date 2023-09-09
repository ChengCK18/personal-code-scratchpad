# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev,curr = None,head # prev will be None as it starts off with outside the range of data

    #     while curr: # interate through each node
    #         nxt = curr.next # to keep original val of the next node to traverse
    #         curr.next = prev # point backwards to prev instead of forward to next
    #         prev= curr # shift prev to curr
    #         curr = nxt # shift curr to next node and repeat

    #     return prev # last prev would be the head

    # def reverseList(self, head: Optional[ListNode],prev=None) -> Optional[ListNode]:
    #     curr = head
    #     if(curr is not None):
    #         nxt = curr.next
    #         curr.next = prev
    #         prev=curr
    #         return self.reverseList(nxt,prev)
    #     else:
    #         return prev
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
    #     if not head:
    #         return None

    #     newHead = head
    #     if(head.next):
    #         newHead = self.reverseList(head.next)
    #         head.next.next = head
    #     head.next = None
        

    #     return newHead