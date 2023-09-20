# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfsValid(node,minLeft,maxRight):
            if not node: # reach end without any invalid condition
                return True
            if(node.val<=minLeft or node.val>=maxRight):
                return False

            return dfsValid(node.left,minLeft,node.val) and dfsValid(node.right,node.val,maxRight)

        return dfsValid(root,float('-inf'),float('+inf'))