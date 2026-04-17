class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [-1] * n
        combos = 0

        def per_step(i):
            
            if i == n:
                return 1
            if i > n:
                return 0
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = per_step(i + 1) + per_step(i+2)
            print(i, cache[i])
            return cache[i]
        
        return per_step(0)
        

