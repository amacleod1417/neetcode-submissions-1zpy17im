class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        right = 0
        left = 0
        seen = {}
        length = 0

        for right, i in enumerate(s): 
            if i in seen and seen[i] >= left:
                left = seen[i] + 1
            seen[i] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
