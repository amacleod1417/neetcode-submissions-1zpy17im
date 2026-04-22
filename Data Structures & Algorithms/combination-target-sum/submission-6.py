class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        sub = []

        def rec(i, total):

            if i >= len(nums):
              
                return

            if sub in res:
                
                return 

            if total > target:
              
                return

            if total == target:
                
                res.append(sub.copy())
                return
             
                
            sub.append(nums[i])
            rec(i, total + nums[i])
            sub.pop()
            rec(i+1, total)
        
        rec(0, 0)
        return res

        

            


        