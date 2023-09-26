# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if(not preorder or not inorder):
            return None


        result_root = TreeNode(preorder[0])
        in_order_index = inorder.index(result_root.val)

        result_root.left = self.buildTree(preorder[1:in_order_index+1],inorder[:in_order_index])
        result_root.right = self.buildTree(preorder[in_order_index+1:],inorder[in_order_index+1:])


        return result_root