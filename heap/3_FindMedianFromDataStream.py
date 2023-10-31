# SOLUTION TLE 17/21 , heap solution but not an optimized solution, to refer to solution
class MedianFinder:

    def __init__(self):
        self.maxHeap =[]
        self.minHeap =[]

    def addNum(self, num: int) -> None:
        def heapifyMax(size,i) -> None:
            # will terminate when largest == i
            largest = i
            l = 2*i+1
            r = 2*i+2
            if(l < size and self.maxHeap[largest]<self.maxHeap[l]): # check valid left index and check if left is larger than curr node
                largest = l
            if(r < size and  self.maxHeap[largest]<self.maxHeap[r]):
                largest = r

            if(largest != i):#swap needed
                self.maxHeap[i], self.maxHeap[largest] = self.maxHeap[largest],self.maxHeap[i]
                heapifyMax(size, largest)

        def heapifyMin(size,i) -> None:
            # will terminate when largest == i
            smallest = i
            l = 2*i+1
            r = 2*i+2
            if(l < size and self.minHeap[smallest] > self.minHeap[l]): # check valid left index and check if left is larger than curr node
                smallest = l
            if(r < size and  self.minHeap[smallest] > self.minHeap[r]):
                smallest = r
            if(smallest != i):#swap needed
                self.minHeap[i], self.minHeap[smallest] = self.minHeap[smallest],self.minHeap[i]
                heapifyMin(size, smallest)


        def insertMaxHeap(num):
            self.maxHeap.append(num)
            size = len(self.maxHeap)
            for i in range((size//2)-1,-1,-1):
                heapifyMax(size,i)
        def insertMinHeap(num):
            self.minHeap.append(num)
            size = len(self.minHeap)
            for i in range((size//2)-1,-1,-1):
                heapifyMin(size,i)

        insertMaxHeap(num)
        if((len(self.maxHeap)>=1 and len(self.minHeap)>=1 and self.minHeap[0]<self.maxHeap[0])):
            maxHeapVal = self.maxHeap.pop(0)
            size = len(self.maxHeap)
            for i in range((size//2)-1,-1,-1):
                heapifyMax(size,i)
            insertMinHeap(maxHeapVal)


        if(abs(len(self.maxHeap) - len(self.minHeap))>=2):
            if(len(self.minHeap)>len(self.maxHeap)):
                minHeapVal = self.minHeap.pop(0)
                size = len(self.minHeap)
                for i in range((size//2)-1,-1,-1):
                    heapifyMin(size,i)
                # insertMaxHeap(minHeapVal)
                self.maxHeap.insert(0,minHeapVal)
            else:
                maxHeapVal = self.maxHeap.pop(0)
                size = len(self.maxHeap)
                for i in range((size//2)-1,-1,-1):
                    heapifyMax(size,i)
                
                # insertMinHeap(maxHeapVal)
                self.minHeap.insert(0,maxHeapVal)
          


              
               
    def findMedian(self) -> float:
        size = len(self.maxHeap) + len(self.minHeap)
        # print('self.maxHeap => ',self.maxHeap,' self.minHeap => ',self.minHeap)
        if(size % 2 ==0):
            return (self.maxHeap[0]+self.minHeap[0])/2
        else:
            if(len(self.maxHeap)>len(self.minHeap)):
                return self.maxHeap[0]
            else:
                return self.minHeap[0]


        

    


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
