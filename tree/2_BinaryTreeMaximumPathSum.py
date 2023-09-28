# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
max_val = 0

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global max_val
       
        max_val = root.val

        self.dfsSumPath(root)

        return max_val
       
       

    def dfsSumPath(self,root):
        global max_val
        if not root:
            return 0

        
        leftMax = max(self.dfsSumPath(root.left),0)
        rightMax = max(self.dfsSumPath(root.right),0)

        split_result = leftMax + rightMax + root.val

        max_val = max(split_result,max_val)
    

        return root.val + max(leftMax,rightMax) # no split left AND right



        