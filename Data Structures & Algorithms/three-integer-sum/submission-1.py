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
            target = -1 * sorted_nums[i]
            while left < right:
                if left > i + 1 and sorted_nums[left] == sorted_nums[left - 1]:
                    left = left + 1 
                    continue
                if right < n - 1 and sorted_nums[right] == sorted_nums[right + 1]:
                    right = right - 1 
                    continue
                if sorted_nums[left] + sorted_nums[right] == target:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left = left + 1
                    continue
                if sorted_nums[left] + sorted_nums[right] < target:
                    left = left + 1
                elif sorted_nums[left] + sorted_nums[right] > target:
                    right = right - 1
        
        return result 