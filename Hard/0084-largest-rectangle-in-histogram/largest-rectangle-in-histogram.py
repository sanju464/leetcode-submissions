class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Stores indices of increasing heights
        
        # Append a sentinel 0 at the end to force flush any remaining bars in stack
        heights.append(0)
        
        for i, h in enumerate(heights):
            # Maintain monotonic increasing property
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                
                # If stack is empty, it means 'height' was the smallest seen so far
                width = i if not stack else i - stack[-1] - 1
                
                max_area = max(max_area, height * width)
                
            stack.append(i)
            
        return max_area

         