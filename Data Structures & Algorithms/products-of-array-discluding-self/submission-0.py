import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        prefix = []
        suffix = []
        
        for i in range(0, len(nums)):
            prefix.append(math.prod(nums[: i]))
            suffix.append(math.prod(nums[i+1:]))
            product.append(suffix[i] * prefix[i])
        return product

        