class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        if k >= len(nums):
            return len(set(nums)) < len(nums)
        while l < len(nums) - k:
            r = l + k 
            num_set = set()
            for i in range(l, r + 1):
                num_set.add(nums[i])
            if len(num_set) <= k:
                return True
            l += 1
        return False
