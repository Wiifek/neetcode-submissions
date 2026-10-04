class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        left, right = 0, l-1
        maxArea = 0
        while left<right:
            area = (right-left)*min(heights[left],heights[right])
            print(area)
            maxArea = max(maxArea, area)
            if (heights[left]<heights[right]):
                left +=1
            else:
                right -=1
        return maxArea