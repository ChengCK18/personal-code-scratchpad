class Solution:
    def twoSum(self,nums:List[int], target:int) -> List[List[int]]:
        unique_dict = {}
        for index,num in enumerate(nums):

            if(num in unique_dict.keys() and num*2 == target): #Handle duplicates
                return [index,unique_dict[num]]

            unique_dict[num] = index
            if(target-num in unique_dict.keys() and unique_dict[target-num]!=index): #complement, using result from subtraction with target
                return [index,unique_dict[target-num]]
