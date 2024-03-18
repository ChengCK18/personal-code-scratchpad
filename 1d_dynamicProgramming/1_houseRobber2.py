# Beat 98.52 algo speed by eliminating need for two loops
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums)==1:
            return nums[0]

        path1A, path2A = 0,0
        path1B, path2B = 0,0
        for index,n in enumerate(nums):
            if(index < len(nums)-1):
                temp = max(n+path1A,path2A)
                path1A = path2A
                path2A = temp
            if(index>=1):
                temp = max(n+path1B,path2B)
                path1B = path2B
                path2B = temp
        

        return max(path2A,path2B)






# Initial accepted own attempt. Not a fast algo according to benchmark
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        if len(nums)==1:
            return nums[0]


        path1A, path2A = 0,0
        for n in nums[:-1]:
            temp = max(n+path1A,path2A)
            path1A = path2A
            path2A = temp
            
        path1B, path2B = 0,0
        for n in nums[1:]:
            temp = max(n+path1B,path2B)
            path1B = path2B
            path2B = temp

        return max(path2A,path2B)