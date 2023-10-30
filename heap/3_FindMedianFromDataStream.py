class MedianFinder:

    def __init__(self):
        self.vals 

    def addNum(self, num: int) -> None:
        

    def findMedian(self) -> float:
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# SOLUTION TLE 20/21 , not an optimized solution, need heap data struct
# import math

# class MedianFinder:

#     def __init__(self):
#         self.vals=[]
#         self.totalLen = 0
        

#     def addNum(self, num: int) -> None:
#         self.totalLen+=1
#         self.vals.append(num)
#         self.vals = sorted(self.vals)

#     def findMedian(self) -> float:
#         if(self.totalLen == 0):
#             return None

#         if(self.totalLen%2==0):
#             return (self.vals[int((self.totalLen/2)-1)] + self.vals[int(self.totalLen/2)])/2

#         else:
#             return self.vals[math.floor(self.totalLen/2)]
