class Solution:
    def rob(self, nums: List[int]) -> int:
        
        robbed = [-1] * len(nums)
        val = 0
        
        def rec(i):
            if i >= len(nums):
                return 0
                print(robbed)

            if robbed[i] != -1:
                print("again", i)
                return robbed[i]
                
            skip = rec(i+1)
            rob = nums[i] + rec(i+2)
            print(i)

            robbed[i] = max(skip, rob)
            
            return robbed[i]
        
        return rec(0)
            
            
            

            

            