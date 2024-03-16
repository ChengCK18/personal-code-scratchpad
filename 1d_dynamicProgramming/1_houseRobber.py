class Solution:
    def rob(self, nums: List[int]) -> int:
        # [path1,path2,n,n+1,....]
        path1, path2 = 0, 0 # path1(take curr and ind(curr)-2), path2(ignore curr and max of prevs)
        
        for n in nums:
            temp = max(n + path1,path2) # gap scenario or max of prev
            path1 = path2 # n+1 with curr path2(to be path1) on next iter
            path2 = temp

        return path2 # contains max comb after final num
