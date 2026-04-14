class Solution:
    def trap(self, height: List[int]) -> int:
        
        areas = []
        i = 1

        while i < len(height) - 1:
            
            left = max(height[:i])
            right = max(height[i + 1:])

            areas.append(min(left, right) - height[i])
            i+=1
            
            # lefts.append(left)
            # rights.append(right)
        
        i = 0
        max_a = 0
        print(areas)

        total = 0
        for a in areas:
            if a > 0:
                total += a
        
        return total

        

        
    
