# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree_queue = deque([root])
        encoded = []
        while tree_queue:
            for x in range(len(tree_queue)):
                node = tree_queue.popleft()
                if(not node):
                    encoded.append('null')
                    continue
                encoded.append(str(node.val))
              
                tree_queue.append(node.left)
                tree_queue.append(node.right)

       
            for x in range(len(encoded)-1,-1,-1): #to remove trailing None, which are not necessary
                if(encoded[x]!='null'):
                    break
                else:
                    encoded.pop()
        
        result = ','.join(encoded)
        return result

    def deserialize(self, data): ####### IN PROGRESS ####
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        decoded = data.split(',')
        decoded_tree = TreeNode(decoded[0])
        level = 1
        parent = deque([decoded_tree])
        node = None
        while True:
            child_slice = decoded[(2**level)-1:(2**level)-1 +(2**level)]
            if(len(child_slice)==0):
                break

            parent_index = 0
            temp = deque()
            while parent:
                node = parent.popleft()
                print(child_slice[2*parent_index])
                print(child_slice[2*parent_index+1])
                node.left = TreeNode(child_slice[2*parent_index])
                node.right = TreeNode(child_slice[2*parent_index+1])
                temp.append(node.left)
                temp.append(node.right)
                parent_index +=1
                print(node)
            parent = temp

            # print(node)
            level+=1
        
        # print(decoded_tree)
        


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))