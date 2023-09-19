# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tree_queue = deque([root])
        while tree_queue:
            node = tree_queue.popleft()
            if(p.val < node.val and q.val < node.val):
                tree_queue.append(node.left)
            elif (p.val > node.val and q.val > node.val):
                tree_queue.append(node.right)
            else:
                return node