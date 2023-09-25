# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def sortedDfs(node):
            if(not root.left and not root.right):
                return [node.val]

            result_l = []
            result_r = []
            if(node.left):
                result_l = sortedDfs(node.left)
            if(node.right):
                result_r = sortedDfs(node.right)

            combined = result_l + [node.val] + result_r
            return combined



        result = sortedDfs(root)
        return result[k-1]

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     tree_stack = []
    #     curr = root
    #     index = 0 #number of sorted nums


    #     while curr or tree_stack:
    #         while curr: # go all the way to the left most node (smallest val)
    #             tree_stack.append(curr) # append all the node along the way
    #             curr = curr.left

    #         curr = tree_stack.pop() # start processing from the leftmost node
    #         index+=1
    #         if(index==k):
    #             return curr.val
    #         curr = curr.right # process the right nodes starting from leftmost nodes