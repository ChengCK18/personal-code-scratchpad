# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)

        curr1 = l1
        curr2 = l2
        resCurr = result
        prev = None
        while curr1 or curr2:

            total = resCurr.val + (curr1.val if curr1 else 0) +  (curr2.val if curr2 else 0)
            if(total>=10):
                resCurr.val = total % 10
                resCurr.next = ListNode(1)
                prev = resCurr
                resCurr = resCurr.next

            else:
                resCurr.val = total
                resCurr.next = ListNode(0)
                prev = resCurr
                resCurr = resCurr.next
        
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        if(resCurr.val == 0): # remove trailing 0
            prev.next = None

    

        return result
            

        