# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         target = 0
#         main = {}
#         main_result = []
#         for index,num in enumerate(nums):
#             result = self.twoSum(nums[:index]+nums[index+1:],target-num,num)
#             for res in result:
#                 if(str(res) not in main.keys()):
#                     main[str(res)] = 1
#                     main_result.append(res)
#         return main_result

#     def twoSum(self, nums:List[int],target,given) -> List[List[int]]:
#         main_dict = {}
#         result = []

#         for index, num in enumerate(nums):
#             if (num in main_dict.keys() and num*2 == target):
#                 sums = sorted([num,num,given])
#                 result.append(sums)
#                 continue
#             main_dict[num] = index
#             complement = target-num
#             if(complement in main_dict.keys() and index != main_dict[complement]):
#                 sums = sorted([num, nums[main_dict[complement]],given])
#                 result.append(sums)
#         return result
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        sorted_nums = sorted(nums)
        result = []


        for index,x in enumerate(sorted_nums):
            if(index >0 and x ==sorted_nums[index-1]):#ignore duplicates
                continue

            left = index+1
            right = len(sorted_nums)-1
            while left<right:
                if(x + sorted_nums[left] +sorted_nums[right] > target):
                    right -=1
                elif(x + sorted_nums[left] +sorted_nums[right] < target):
                    left +=1
                elif(x + sorted_nums[left] +sorted_nums[right] == target):
                    result.append([x,sorted_nums[left],sorted_nums[right]])
                    left+=1
                    while(sorted_nums[left] == sorted_nums[left-1] and left<right): # traverse through duplicate
                        left+=1


        return result











