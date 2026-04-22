class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        right = len(nums) - 1
        left = 0

        if nums[0] == min(nums):
            return nums[0]

        while left <= right:
            if nums[left] < nums[left + 1]:
                left += 1
            else:
                return nums[left + 1]
            
            if nums[right] > nums[right - 1]:
                right -= 1
            else:
                return nums[right]
        


