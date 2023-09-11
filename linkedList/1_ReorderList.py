class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None # split into two

        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first = head
        second = prev
        while second:
            tmp1 ,tmp2 = first.next , second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2









        # Not working attempt
        # curr = head
        # index = 0
        # nxt = None
        # while curr:
        #     if(index%2==0):
        #         temp = curr
        #         while True:
        #             if(temp.next and temp.next.next):
        #                 temp = temp.next
        #             else:
        #                 curr.next.next = None
        #                 break
        #         nxt = curr.next
        #         curr.next = temp
        #         curr = curr.next
        #     else:
        #         curr.next = nxt
        #         curr = curr.next
        #     index +=1
        # print(curr)
