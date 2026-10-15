class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 1
        res = list(s)
        best = 0
        
        freq = {}
        max_freq = 0
        
        while right < len(res) + 1:
      
            new_char = res[right - 1]
            freq[new_char] = freq.get(new_char, 0) + 1
            if freq[new_char] > max_freq:
                max_freq = freq[new_char]
    
            window_len = right - left
            
            if window_len - max_freq <= k:
                if window_len > best:
                    best = window_len
                right += 1
            else:
    
                left_char = res[left]
                freq[left_char] -= 1
                freq[new_char] -= 1 
                
                left += 1
                
        return best
