class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counteri = -1
        counterj = 0
        for i in range(0,len(nums)):
            counteri += 1
            for j in range(i+1, len(nums)):
                counterj +=1
                if nums[i] + nums[j] == target:
                    if i <= j:
                        return [i,j]
                    else:
                        return[j,i]

                

                