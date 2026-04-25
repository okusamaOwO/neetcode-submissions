class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        initial = []
        n = len(nums)
        def tryy(i):
            if i == n:
                result.append(initial.copy())
                return
            for j in range(2):
                # accept to append i
                if j == 0:
                    initial.append(nums[i])
                else:
                    initial.pop()
                tryy(i+1)
                
        tryy(0)
        return result 