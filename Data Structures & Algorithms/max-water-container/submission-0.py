class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        
        max_area = 0
        
        while left < right:
            # Calculate the area with current bars
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            
            # Update max_area if this is larger
            max_area = max(max_area, area)
            
            # Move the pointer with the smaller height towards the other pointer
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
