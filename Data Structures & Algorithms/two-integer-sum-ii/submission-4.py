class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        j = len(numbers) - 1
        i = 0
        sum = []
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            
            elif numbers[i] + numbers[j] < target:
                i += 1
            
            else:
                sum.append(i + 1)
                sum.append(j + 1)
                return sum