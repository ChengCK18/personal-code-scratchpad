# ref solution
class Solution:
    def climbStairs(self, n: int) -> int:
        oneStep,twoStep = 1,1

        for i in range(n-1):
            temp = oneStep
            oneStep = oneStep+twoStep
            twoStep = temp   
        return oneStep     

# initial attempt
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if(n == 1):
#             return 1
#         if (n==0):
#             return 0
#         dp_1d = [0 for x in range(n)]
#         for i in range(len(dp_1d)-1, -1, -1):
#             if(i==len(dp_1d)-1 or i==len(dp_1d)-2): # final step or 1 step before final
#                 dp_1d[i] = 1

#             if(i>len(dp_1d)-3):
#                 continue

#             dp_1d[i] = dp_1d[i+1] + dp_1d[i+2]


#         return dp_1d[0]+dp_1d[1]
            

