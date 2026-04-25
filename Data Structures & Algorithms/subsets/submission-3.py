class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def tryy(level):
            if level == len(nums):
                result.append(path.copy())
                return
            # if chon
            path.append(nums[level])
            tryy(level+1)
            path.pop()
            tryy(level+1)
        tryy(0)
        return result