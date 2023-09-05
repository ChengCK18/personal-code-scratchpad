class Solution:
    def isValid(self, s: str) -> bool:
        order =[]

        for char in s:
            if(char == '(' or char == '{' or char=='['):
                order.append(char)
            else:
                if(len(order)==0):
                    return False
                if(char == ')'):
                    if order.pop()!='(':
                        return False
                elif(char == '}'):
                    if order.pop()!='{':
                        return False
                elif(char == ']'):
                    if order.pop()!='[':
                        return False

        if(len(order)!=0):
            return False


        return True

