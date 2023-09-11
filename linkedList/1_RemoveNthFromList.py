class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        list_size = 0
        while curr:
            curr = curr.next
            list_size+=1

        curr = head
        target = list_size - n
        index = 0

        if(target == 0):
            return head.next

        while curr:

            if(index+1 == target):
                curr.next = curr.next.next if curr.next.next else None
                break
            curr = curr.next
            index +=1


        return head