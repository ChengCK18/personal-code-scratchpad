# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return root

        tree_queue = deque([root])
        result = []
        while tree_queue:
            level_result = []
            for x in range(len(tree_queue)):
                node = tree_queue.popleft()
                level_result.append(node.val)

                if(node.left):
                    tree_queue.append(node.left)
                if(node.right):
                    tree_queue.append(node.right)
            result.append(level_result)

        return result

        # if(not root):
        #     return []
        # tree_queue = deque([root])
        # result = []
        # level = 0
        # while tree_queue:
        #     nodes = []
        #     level_result = []
        #     for x in range(2**level):
        #         node = tree_queue.popleft()
        #         nodes.append(node)
        #         level_result.append(node.val)
        #         if(len(tree_queue)==0):
        #             break

        #     for node in nodes:
        #         if(node.left):
        #             tree_queue.append(node.left)
        #         if(node.right):
        #             tree_queue.append(node.right)
        #     result.append(level_result)
        #     level+=1
        # return result