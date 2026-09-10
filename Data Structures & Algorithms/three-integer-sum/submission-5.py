class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:

                if nums[j] + nums[k] == target:
                    works = [nums[i], nums[j], nums[k]]

                    if works not in result:
                        result.append(works)

                    j += 1
                    k -= 1

                elif nums[j] + nums[k] > target:
                    k -= 1

                else:
                    j += 1

        return result