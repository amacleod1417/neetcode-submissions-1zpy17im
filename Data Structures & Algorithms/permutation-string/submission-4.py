class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        right = len(s1) - 1
        left = 0
        freq2 = [0] * 26

        if len(s1) > len(s2):
            return False
        
        for i in s1:
            index = ord(i) - ord('a')
            freq2[index] += 1

        while right < len(s2):
            freq1 = [0] * 26

            for i in range(left, right + 1):
                char = s2[i]
                index = ord(char) - ord('a')
                freq1[index] += 1
            
            print(freq1)
            
            if freq1 == freq2:
                return True
            
            else:
                left += 1
                right += 1
        
        return False







            


        
    

            
           


