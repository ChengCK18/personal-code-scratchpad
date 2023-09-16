# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(not subRoot):
            return True
        if(not root):
            return False

        if(self.sameTree(root,subRoot)):
            return True


        result_left = self.isSubtree(root.left,subRoot)
        result_right = self.isSubtree(root.right,subRoot)


        return result_left or result_right



    def sameTree(self,p,q):
        if(not p and not q):
            return True


        if(p and q and p.val == q.val):
            result_left = self.sameTree(p.left,q.left)
            result_right = self.sameTree(p.right,q.right)
            return result_left and result_right

        return False