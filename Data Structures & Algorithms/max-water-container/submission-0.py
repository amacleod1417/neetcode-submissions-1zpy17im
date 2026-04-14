class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_a = 0

        while i < j:

            current_a = min(heights[i], heights[j]) * (j - i)
            if  current_a > max_a:
                max_a = current_a
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_a
            
        