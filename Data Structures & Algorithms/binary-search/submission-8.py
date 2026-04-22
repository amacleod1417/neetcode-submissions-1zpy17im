class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums) - 1

        if nums[i] == target:
            return i

        if nums[j] == target:
            return j



        while j - i > 1:


            mid = math.floor((i + j) / 2)
        
            if nums[mid] < target:
                i = mid
                
            elif nums[mid] > target:
                j = mid

            else: 
                return mid

        return -1