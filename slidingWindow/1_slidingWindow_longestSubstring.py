class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left_ptr = 0
        max_seq = 0

        for right_ptr in range(len(s)):
            while s[right_ptr] in unique:
                unique.remove(s[left_ptr])
                left_ptr+=1
            unique.add(s[right_ptr])
            max_seq = max(max_seq,len(unique))

        return max_seq

    # def lengthOfLongestSubstring(self, s: str) -> int: # brute force
    #     left_ptr = 0
    #     max_seq = 0
    #     if(len(s)==1):
    #         return 1
    #     if(len(s)==2):
    #         if(s[0]!=s[1]):
    #             return 2
    #         else:
    #             return 1
    #     while (left_ptr<=len(s)-2):
    #         right_ptr = left_ptr+1
    #         if(s[left_ptr]==s[right_ptr]):
    #             if(max_seq<1):
    #                 max_seq = 1
    #             left_ptr +=1
    #             continue

    #         unique={}
    #         unique[s[left_ptr]] = 1
    #         continuous=1
    #         while (right_ptr<len(s)):
    #             if(s[right_ptr] not in unique.keys()):
    #                 unique[s[right_ptr]] = 1
    #                 continuous += 1
    #             else:
    #                 break
    #             right_ptr +=1

    #         if(continuous>max_seq):
    #             max_seq = continuous

    #         left_ptr +=1

    #     return max_seq






    # def lengthOfLongestSubstring(self, s: str) -> int: #misunderstood question, thought sequence of continous chars with ascending/descending orders
    #     main_left_ptr = 0
    #     max_seq = 1
    #     if(len(s)==0):
    #         return 0
    #     while (main_left_ptr<len(s)-1):
    #         left_ptr = main_left_ptr
    #         right_ptr = main_left_ptr+1

    #         if(s[left_ptr] == s[right_ptr]): #same chars
    #             main_left_ptr+=1
    #             continue

    #         descending_continuous = 1
    #         ascending_continous = 1
    #         # print(s[left_ptr],'-----------',s[right_ptr])
    #         if(ord(s[left_ptr])>ord(s[right_ptr])):
    #             # print('descending')
    #             descending_continuous+=1
    #             while True:
    #                 left_ptr+=1
    #                 right_ptr+=1
    #                 if(right_ptr>=len(s)):
    #                     break
    #                 if(ord(s[left_ptr])>ord(s[right_ptr])):
    #                     descending_continuous+=1
    #                 else:
    #                     break
    #         elif(ord(s[left_ptr])<ord(s[right_ptr])):
    #             # print('ascending')
    #             ascending_continous+=1
    #             while True:
    #                 left_ptr+=1
    #                 right_ptr+=1
    #                 if(right_ptr>=len(s)):
    #                     break
    #                 if(ord(s[left_ptr])<ord(s[right_ptr])):
    #                     ascending_continous+=1
    #                 else:
    #                     break

    #         max_both = max(descending_continuous,ascending_continous)
    #         if(max_both >max_seq):
    #             max_seq = max_both
    #         main_left_ptr+=1

    #     return max_seq









