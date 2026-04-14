class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) -1
        s = s.lower()
        length = len(s)
        while i < j:
            
            while i<j and (s[i].isalnum()) == False:
                i+=1
                length -= 1
            while i<j and (s[j].isalnum()) == False:
                j-=1
                length -=1
                 
            if s[i] == s[j]:
                j-=1
                i+=1
            else:
                return False
        return True
    
    
            

        

