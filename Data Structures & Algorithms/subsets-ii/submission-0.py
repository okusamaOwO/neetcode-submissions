class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        def tryy(i):
            if i == len(nums):
                result.append(path.copy())
                return
            # include nums[i]
            path.append(nums[i])
            tryy(i+1)
            # ignore nums[i] 
            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i = i + 1
            tryy(i+1)
        tryy(0)
        return result 