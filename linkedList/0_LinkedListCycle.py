class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        history = set()

        while curr:
            if(curr not in history):
                history.add(curr)
                curr = curr.next
            else:
                return True
        return False


        # Array slow in lookup, use dict/set instead, lookup O(1)
        # curr = head
        # history = []

        # while curr:
        #     if(curr not in history):
        #         history.append(curr)
        #         curr = curr.next
        #     else:
        #         return True
        # return False


