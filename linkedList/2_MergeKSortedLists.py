# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:





    # Attempt at reusing mergeTwo function. Runtime 16.51% much slower. O(n^2) ###############################
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # def mergeTwo(list1,list2):
        #     dummy = ListNode()
        #     curr = dummy

        #     while list1 and list2:
        #         if(list1.val < list2.val):
        #             curr.next = list1
        #             list1 = list1.next

        #         else:
        #             curr.next = list2
        #             list2 = list2.next

        #         curr = curr.next

        #     if(list1):
        #         curr.next = list1
        #     if(list2):
        #         curr.next = list2

        #     return dummy.next

        # if not lists:
        #    return None
        # merged_result = lists[0]

        # for i in range(1,len(lists)):
        #     merged_result = mergeTwo(merged_result,lists[i])

        # return merged_result



        # Runtime beat 99.87% of solution. O(n^2)###############################################
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # dummy = ListNode()
        # curr = dummy

        # main_arr = []
        # for main in lists:
        #     main_node = main
        #     while main_node:
        #         main_arr.append(main_node)
        #         main_node = main_node.next

        # sorted_main_arr = sorted(main_arr, key=lambda x:x.val)


        # for item in sorted_main_arr:
        #     curr.next = item
        #     curr = curr.next

        # return dummy.next




    # Merge sort style O(n log k)###################################################
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #           if not lists:
    #        return None

    #     while len(lists)>1:
    #         mergedResult = []

    #         for i in range(0, len(lists),2): # merge sort algo style
    #             l1 = lists[i]
    #             l2 = lists[i+1] if i+1 < len(lists) else None
    #             mergedResult.append(self.mergeTwo(l1,l2))
    #         lists = mergedResult
    #     return lists[0]


    # def mergeTwo(self,list1,list2):
    #     dummy = ListNode()
    #     curr = dummy

    #     while list1 and list2:
    #         if(list1.val < list2.val):
    #             curr.next = list1
    #             list1 = list1.next

    #         else:
    #             curr.next = list2
    #             list2 = list2.next

    #         curr = curr.next

    #     if(list1):
    #         curr.next = list1
    #     if(list2):
    #         curr.next = list2

    #     return dummy.next