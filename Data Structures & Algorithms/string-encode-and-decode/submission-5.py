from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        combined_str = ""
        for i in strs:
            combined_str = combined_str + str(len(i)) + "#" + i
        return combined_str


    def decode(self, s: str) -> List[str]:
        seperated_str = [] 
        entry = ""

        while (len(s) != 0):
            delim = s.index('#')
            length = int(s[0:delim])
            word = s[delim + 1: delim + length + 1]
            seperated_str.append(word)
            s = s[delim + 1 +length:]
        
        

        return seperated_str
    
    