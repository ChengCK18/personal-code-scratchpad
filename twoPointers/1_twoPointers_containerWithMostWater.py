class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = int(len(height)-1)
        areas = []
        max_area = 0

        while(left<right):
            lowest_between_two = min(height[left],height[right])
            right_dist = right+1
            left_dist = left+1
            distance =right_dist-left_dist
            area = lowest_between_two * distance

            if(area>max_area):
                max_area = area

            if(height[left]<height[right]):
                left+=1
            else:
                right-=1

        return max_area