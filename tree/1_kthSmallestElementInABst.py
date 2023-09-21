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