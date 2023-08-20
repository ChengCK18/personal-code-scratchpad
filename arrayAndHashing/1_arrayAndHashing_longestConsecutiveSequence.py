# class Solution: # NOT A O(n) SOLUTION, IT'S O(n log n)
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         max_list = []
#         max_seq = 0
#         for x in (nums):
#             if(len(max_list)==0):
#                 max_list.append(x)
#             else:
#                 if(x ==  max_list[-1]):
#                     continue
#                 if(x == max_list[-1]+1):
#                     max_list.append(x)
#                 else:
#                     if(len(max_list)>max_seq):
#                         max_seq=len(max_list)
#                     max_list.clear()
#                     max_list.append(x)

#         if(len(max_list)>max_seq):
#             max_seq=len(max_list)

#         return max_seq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_seq = 0

        for x in numSet:
            if(x-1 not in numSet):# Indicator of a start of a sequence, lookup in set O(1)
                current_seq_length = 1 # element x-1
                while (x+current_seq_length) in numSet:
                    current_seq_length+=1
                max_seq = max(current_seq_length,max_seq)

        return max_seq






