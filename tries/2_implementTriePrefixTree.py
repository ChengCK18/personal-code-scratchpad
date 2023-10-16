class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if(c not in cur.children):
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if(c not in cur.children):
                return False
            cur = cur.children[c]
        return cur.endOfWord # has to end with valid word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if(c not in cur.children):
                return False
            cur = cur.children[c]
     
       
        if(len(cur.children.keys())>0 or cur.endOfWord == True):
            return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)









########## 
# Initial attempt, success 
# but can be improved to use dict instead of list to make lookup much faster
# now algo is somewhat slow as it needs to traverse array for compare child

# from dataclasses import dataclass
# from typing import List

# @dataclass      
# class Node:
#     char:str
#     isWord:bool
#     links:List['Node']

# class Trie:

#     def __init__(self):
#         self.root = []

#     def insertFromRoot(self,word:str)->None: # a helper function to insert fresh chain from root
#         if(len(word)==1):
#             newRootNode = Node(char=word[0], isWord=True, links=[])
#         else:
#             newRootNode = Node(char=word[0], isWord=False, links=[])
#         self.root.append(newRootNode)
#         prev_node = newRootNode

#         for i in range (1,len(word)-1):
#             nextNode = Node(char=word[i], isWord=False,links=[])
#             prev_node.links.append(nextNode)
#             prev_node = nextNode
#         last_node = Node(char=word[len(word)-1], isWord=True,links=[])
#         prev_node.links.append(last_node)


#     def insert(self, word: str) -> None:
#         if(len(self.root)==0): # no existing root found
#            self.insertFromRoot(word)
#         else:
#             # check against existing root char, if any exist, then cont the chain from root
#             node = None
#             for rootNode in self.root:
#                 if(rootNode.char == word[0]):
#                     node = rootNode
            
#             if(node is None): # no common root, insert fresh from root onwards
#                 self.insertFromRoot(word)
#             else: # common root found, continue from common root
#                 for i in range(1,len(word)):# traverse 2nd letter of word onwards
#                     linkFound = False
#                     for link in node.links: # check against all current node's links 
#                         if(link.char == word[i]):
#                             node = link
#                             linkFound = True
                    
#                     if(not linkFound):# no common char found in existing links
#                         newNode = Node(char=word[i], isWord=False,links=[])
#                         node.links.append(newNode)
#                         node = newNode
#                 node.isWord = True #Last charac of the chain
                

#     def search(self, word: str) -> bool:
#         node = None
#         for rootNode in self.root:
#             if(rootNode.char == word[0]):
#                 node = rootNode
#         if node is None: #  no common root
#             return False

#         for char in word[1:]:
#             linkFound = False
#             for link in node.links:
#                 if(char==link.char):
#                     node = link
#                     linkFound = True
#                     break
#             if(not linkFound):
#                 return False
#         if(node.isWord):
#             return True
#         else:
#             return False
        
        
#     def startsWith(self, prefix: str) -> bool:
#         node = None
#         for rootNode in self.root:
#             if(rootNode.char == prefix[0]):
#                 node = rootNode
#         if node is None: #  no common root
#             return False

#         for char in prefix[1:]:
#             linkFound = False
#             for link in node.links:
#                 if(char==link.char):
#                     node = link
#                     linkFound = True
#                     break
#             if(not linkFound):
#                 return False
        
#         return True
                


#     # def startsWith(self, prefix: str) -> bool: # recursive approach, slow and overcomplicated
#     #     def recursiveSearch(links):
#     #         validWord = False
#     #         for node in links:
#     #             if(len(node.links)>=1):
#     #                 validWord = recursiveSearch(node.links)
#     #             if(node.isWord):
#     #                 return True

#     #         return validWord
                
#     #     # condition: At least 1 isWord true with the stated prefix
#     #     node = None
#     #     for rootNode in self.root:
#     #         if(rootNode.char == prefix[0]):
#     #             node = rootNode
#     #     if(not node): # no common root node
#     #         return False
#     #     if(node and len(prefix)==1 and node.isWord): # common root, single prefix, first node is a word
#     #         return True

        
#     #     for i in range (1,len(prefix)):
#     #         linkFound = False
#     #         for link in node.links:
#     #             if(link.char == prefix[i]):
#     #                 node = link
#     #                 linkFound = True
            
#     #         if(not linkFound): # no match
#     #             return False
        
#     #     if(node.isWord): #end of prefix is a word, directly return true
#     #         return True

        
#     #     return recursiveSearch(node.links)
#     #     # else continue traversing through all the links and sublinks of the last node and 
#     #     # find at least one node with isWord = True


# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)
