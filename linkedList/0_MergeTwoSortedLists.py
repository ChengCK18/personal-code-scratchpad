# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = ListNode() 
        tail = result_list
        
        while list1 and list2:
            if(list1.val<list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
              
        if(list1): # there is still remaining elements in list1, join it with the result list
            tail.next = list1

        elif(list2): # there is still remaining elements in list2, join it with the result list
            tail.next = list2

        return result_list.next #to skip the initial node with value 0
