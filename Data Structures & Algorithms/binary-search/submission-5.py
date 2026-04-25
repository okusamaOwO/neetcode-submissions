class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            middle = int((low + high) / 2)
            if nums[middle] == target:
                return middle
            if target < nums[middle]:
                high = middle - 1
            else:
                low = middle + 1
        return -1 