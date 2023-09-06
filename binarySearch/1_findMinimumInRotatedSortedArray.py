class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        min_val = nums[0]

        while left<=right:
            if(nums[left]<nums[right]): #already sorted without rotation
                return min(nums[left],min_val)

            middle = (left+right)//2
            min_val = min(min_val,nums[middle])

            if(nums[middle]>=nums[left]):
                left = middle+1
            else:
                right = middle-1



        return min_val
        # left=0
        # middle=int(len(nums)/2)
        # right=len(nums)-1
        # min_val = nums[middle]

        # if(nums[left]<nums[right]):
        #     return nums[left]
        # if(nums[middle]>=nums[left]):
        #     while middle<len(nums):
        #         if(nums[middle]<min_val):
        #             min_val = nums[middle]
        #         middle+=1
        # else:
        #     while middle>=0:
        #         if(nums[middle]<min_val):
        #             min_val = nums[middle]
        #         middle-=1

        # return min_val