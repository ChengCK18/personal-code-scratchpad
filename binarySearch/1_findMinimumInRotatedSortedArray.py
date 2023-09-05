class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        middle=int(len(nums)/2)
        right=len(nums)-1
        min_val = nums[middle]

        if(nums[left]<nums[right]):
            return nums[left]
        if(nums[middle]>=nums[left]):
            while middle<len(nums):
                if(nums[middle]<min_val):
                    min_val = nums[middle]
                middle+=1
        else:
            while middle>=0:
                if(nums[middle]<min_val):
                    min_val = nums[middle]
                middle-=1

        return min_val