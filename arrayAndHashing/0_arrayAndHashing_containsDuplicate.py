class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        for index,num in enumerate(nums):
            if(num in unique.keys()):
                return True
            unique[num] = num

        return False