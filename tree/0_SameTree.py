# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #DFS approach
        if((p is None and q is not None) or (q is None and p is not None)): #Only either one None
            return False
        if(not p and not q):#Both None
            return True
        if(p.val == q.val):
            result_left = self.isSameTree(p.left,q.left)
            result_right = self.isSameTree(p.right,q.right)
            return result_left and result_right
        else:
            return False

        return True


        #BFS approach
        # if(p==q):#empty tree for both
        #     return True
        # if not p or not q: # either one is empty tree
        #     return False

        # queue_p = deque([p])
        # queue_q = deque([q])
        # while queue_p:
        #     for i in range(len(queue_p)):

        #         node_p = queue_p.popleft()
        #         node_q = queue_q.popleft()

        #         if(node_p is None and node_q is not None):
        #             return False
        #         if(node_q is None and node_p is not None):
        #             return False

        #         if(node_p is None and node_q is None):
        #             continue
        #         if(node_p.val != node_q.val):
        #             return False