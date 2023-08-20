class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     main_dict = {}
    #     nums = sorted(nums) #n log n

    #     for num in nums:
    #         if(num in main_dict.keys()):
    #             main_dict[num] +=1
    #         else:
    #             main_dict[num] = 1

    #     sorted_list = sorted(main_dict.items(), key = lambda item:item[1], reverse=True)
    #     result = []
    #     for x in sorted_list:
    #         result.append(x[0])

    #     return result[:k]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            unique_dict = collections.Counter(nums) #return a Counter object with unique element key and frequency
            sorted_dict = sorted(unique_dict.items(),key= lambda item:item[1],reverse=True)
            result = [x[0] for x in sorted_dict ]
            return result[:k]

















