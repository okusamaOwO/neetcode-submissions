class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        result = []
        for i in range(n-2):
            if i >= 1 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                sum_ = sorted_nums[left] + sorted_nums[right]
                target = -1 * sorted_nums[i]
                if sum_ < target:
                    left = left + 1
                elif sum_ > target:
                    right = right - 1
                else:
                    result.append([sorted_nums[left], sorted_nums[right], sorted_nums[i]])
                    # skip duplicates
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left = left + 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1 
        return result 