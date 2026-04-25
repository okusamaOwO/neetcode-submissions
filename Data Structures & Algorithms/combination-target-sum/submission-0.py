class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        def tryy(remaining_target, i):
            if remaining_target == 0:
                result.append(path.copy())
                return
            if remaining_target < 0:
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                tryy(remaining_target - nums[j], j)
                path.pop()
        tryy(target,0)
        return result