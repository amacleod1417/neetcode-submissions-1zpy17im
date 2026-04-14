class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = -1
        arrays = [0] * len(strs)
        for i in strs:
            alph = [0] * 26
            counter +=1
            for char in i:
                value = ord(char)
                diff = value - 97
                alph[diff] += 1
            
            arrays[counter] = tuple(alph)

        index = 0
        map = {}
        for p in arrays:
            if p in map:
                map[p].append(strs[index])
            else:
                map[p] = [strs[index]]
            index += 1
        
        return list(map.values())
  

            




            
