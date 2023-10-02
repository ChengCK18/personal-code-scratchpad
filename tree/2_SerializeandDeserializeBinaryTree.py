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
        if(not root):
            return 'null'
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
    

    #deserialize FAIL: [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
    def deserialize(self, data): # child slice must be based on number of non null parents. To be modified.
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
  
        if(data == 'null'):
            return []

        decoded = data.split(',')
        decoded_tree = TreeNode(decoded[0])
        level = 1
        parent = deque([decoded_tree])
        while True:
            level = len(parent)
            child_slice = decoded[(2**level)-1:(2**level)-1 +level]
            if(len(child_slice)==0):
                break
            # print(child_slice)
            parent_index = 0
            temp = deque()
            while parent:
                node = parent.popleft()
                if(not node):
                    continue
                if((2*parent_index)<len(child_slice) and child_slice[2*parent_index] != 'null'):
                    node.left = TreeNode(child_slice[2*parent_index])
                if((2*parent_index+1)<len(child_slice) and child_slice[2*parent_index+1] != 'null'):
                    node.right = TreeNode(child_slice[2*parent_index+1])
                temp.append(node.left)
                temp.append(node.right)
                parent_index +=1
                # print(node)
            
            parent = temp
            print(len(parent))

            
            level+=1
       
        return decoded_tree
        


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))