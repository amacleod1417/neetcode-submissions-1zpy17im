class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for i in nums:
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1

        topvals = []

        while k != 0:
            big_num = max(freq, key=freq.get)
            topvals.append(big_num)
            freq.pop(big_num)
            k = k-1
        
        return topvals

            
        

                
            


        
