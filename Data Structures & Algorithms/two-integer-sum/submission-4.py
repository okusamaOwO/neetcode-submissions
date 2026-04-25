class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                if x + y == target :
                    result = [i, j+i+1]
                    return result
        return result

            