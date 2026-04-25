class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtrack(choices, i):
            if i == len(nums):
                print(path)
                result.append(path.copy())
                return
            for choice in choices:
                if choice == 1:
                    path.append(nums[i])
                    backtrack(choices,i+1)
                    path.pop()
                else:
                    backtrack(choices,i+1)
        backtrack([1,2], 0)
        return result
                    
                    
